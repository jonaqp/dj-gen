from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.mixins import (
    AuthListView, AuthCreateView, AuthUpdateView, AuthDeleteView
)
from project_name.apps.restaurant.models import RestaurantTable
from .forms import ReservationForm, ReservationTableForm
from .formset import ReservationMenuFormSet
from .models import Reservation, ReservationMenu, ReservationTable


# RESTAURANT
class ReservationList(AuthListView):
    template_name = 'themes/pages/reservation/reservation/reservation_list.html'
    model = Reservation
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Reservation List")
        return context


class ReservationCreate(AuthCreateView):
    template_name = 'themes/pages/reservation/reservation/reservation_form.html'
    model = Reservation
    success_url = reverse_lazy('reservation_app:reservation:list')
    form_class = ReservationForm

    def get_initial(self):
        super().get_initial()
        reservation_id = self.kwargs.get("pk", None)
        self.parameter = dict(paciente=reservation_id)
        return self.parameter

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.form_mesa = ReservationTableForm()
        self.formset_menu = ReservationMenuFormSet()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_mesa = ReservationTableForm(request.POST)
        formset_menu = ReservationMenuFormSet(request.POST)
        if form.is_valid() and form_mesa.is_valid() and formset_menu.is_valid():
            return self.frm_valid(form, form_mesa, formset_menu)
        else:
            return self.frm_invalid(form, form_mesa, formset_menu)

    def frm_valid(self, form, form_mesa, formset_menu):
        with transaction.atomic():
            self.object = form.save()
            form_mesa.save(reservation=self.object, commit=False)
            formset_menu.instance = self.object
            formset_menu.save()

        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, form_mesa, formset_menu):
        self.form = form
        self.form_mesa = form_mesa
        self.formset_menu = formset_menu
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_mesa"] = self.form_mesa
        context["formset_menu"] = self.formset_menu
        context["text_central"] = _("reservation create")
        return context


class ReservationUpdate(AuthUpdateView):
    template_name = 'themes/pages/reservation/reservation/reservation_form.html'
    model = Reservation
    success_url = reverse_lazy('reservation_app:reservation:list')
    form_class = ReservationForm

    def get_initial(self):
        super().get_initial()
        reservation_id = self.kwargs.get("pk", None)
        self.parameter = dict(paciente=reservation_id)
        return self.parameter

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        _mesa = ReservationTable.objects.get(reservation=self.object)
        self.form_mesa = ReservationTableForm(instance=_mesa)
        self.formset_menu = ReservationMenuFormSet(instance=self.object)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        _mesa = ReservationTable.objects.get(reservation=self.object)
        form_mesa = ReservationTableForm(request.POST, instance=_mesa)
        formset_menu = ReservationMenuFormSet(request.POST, instance=self.object)

        if form.is_valid() and form_mesa.is_valid() and formset_menu.is_valid():
            return self.frm_valid(form, form_mesa, formset_menu)
        else:
            return self.frm_invalid(form, form_mesa, formset_menu)

    def frm_valid(self, form, form_mesa, formset_menu):
        with transaction.atomic():
            reservation_table = ReservationTable.objects.get(reservation=self.object)
            RestaurantTable.objects.filter(pk=reservation_table.id).update(is_occupied=False)

            mesa = self.request.POST.get('restaurantTable', None)
            finish = self.request.POST.get('is_finished', None)
            if mesa:
                RestaurantTable.objects.filter(pk=mesa).update(is_occupied=True)
            if finish:
                RestaurantTable.objects.filter(pk=mesa).update(is_occupied=False)
            self.object = form.save()
            form_mesa.save(reservation=self.object, commit=False)
            formset_menu.instance = self.object
            formset_menu.save()

        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, form_mesa, formset_menu):
        self.form = form
        self.form_mesa = form_mesa
        self.formset_menu = formset_menu
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_mesa"] = self.form_mesa
        context["formset_menu"] = self.formset_menu
        context["text_central"] = _("reservation update")
        return context

class ReservationDelete(AuthDeleteView):
    template_name = 'themes/pages/reservation/reservation/reservation_confirm_delete.html'
    model = Reservation
    success_url = reverse_lazy('reservation_app:reservation:list')


# RESVATION MESA
class ReservationMesaList(AuthListView):
    template_name = 'themes/pages/reservation/mesa/reservation_mesa_list.html'
    model = RestaurantTable
    paginate_by = 10

    def get_queryset(self):
        queryset = RestaurantTable.objects.all().order_by('is_occupied')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Table List")
        return context
