from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.mixins import (
    AuthListView, AuthUpdateView
)
from project_name.apps.reservation.models import ReservationMenu
from .forms import ReservationMenuForm


# RESTAURANT
class PedidoList(AuthListView):
    template_name = 'themes/pages/kitchen/pedido/pedido_list.html'
    model = ReservationMenu
    paginate_by = 10

    def get_queryset(self):
        queryset = ReservationMenu.objects.filter(is_kitchen_completed=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Order")
        return context


class PedidoUpdate(AuthUpdateView):
    template_name = 'themes/pages/kitchen/pedido/pedido_form.html'
    model = ReservationMenu
    success_url = reverse_lazy('kitchen_app:pedido:list')
    form_class = ReservationMenuForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Order Completed")
        return context
