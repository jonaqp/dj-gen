from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.mixins import (
    AuthListView, AuthCreateView, AuthUpdateView, AuthDeleteView
)
from .forms import RestaurantForm, RestaurantMenuForm, RestaurantTable
from .models import Restaurant, RestaurantTable, RestaurantMenu


# RESTAURANT
class RestaurantList(AuthListView):
    template_name = 'themes/pages/restaurant/restaurant/restaurant_list.html'
    model = Restaurant
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Restaurant")
        return context


class RestaurantCreate(AuthCreateView):
    template_name = 'themes/pages/restaurant/restaurant/restaurant_form.html'
    model = Restaurant
    success_url = reverse_lazy('restaurant_app:restaurant:list')
    form_class = RestaurantForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("restaurant create")
        return context


class RestaurantUpdate(AuthUpdateView):
    template_name = 'themes/pages/restaurant/restaurant/restaurant_form.html'
    model = Restaurant
    success_url = reverse_lazy('restaurant_app:restaurant:list')
    form_class = RestaurantForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("restaurant update")
        return context


class RestaurantDelete(AuthDeleteView):
    template_name = 'themes/pages/restaurant/restaurant/restaurant_confirm_delete.html'
    model = Restaurant
    success_url = reverse_lazy('restaurant_app:restaurant:list')


# MESA
class MesaList(AuthListView):
    template_name = 'themes/pages/restaurant/mesa/mesa_list.html'
    model = RestaurantTable
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Restaurant Mesa List")
        return context


class MesaCreate(AuthCreateView):
    template_name = 'themes/pages/restaurant/mesa/mesa_form.html'
    model = RestaurantTable
    success_url = reverse_lazy('restaurant_app:mesa:list')
    form_class = RestaurantTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Mesa create")
        return context


class MesaUpdate(AuthUpdateView):
    template_name = 'themes/pages/restaurant/mesa/mesa_form.html'
    model = RestaurantTable
    success_url = reverse_lazy('restaurant_app:mesa:list')
    form_class = RestaurantTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Mesa update")
        return context


class MesaDelete(AuthDeleteView):
    template_name = 'themes/pages/restaurant/mesa/mesa_confirm_delete.html'
    model = RestaurantTable
    success_url = reverse_lazy('restaurant_app:mesa:list')


# MENU
class MenuList(AuthListView):
    template_name = 'themes/pages/restaurant/menu/menu_list.html'
    model = RestaurantMenu
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("Restaurant Menu List")
        return context


class MenuCreate(AuthCreateView):
    template_name = 'themes/pages/restaurant/menu/menu_form.html'
    model = RestaurantMenu
    success_url = reverse_lazy('restaurant_app:menu:list')
    form_class = RestaurantMenuForm


class MenuUpdate(AuthUpdateView):
    template_name = 'themes/pages/restaurant/menu/menu_form.html'
    model = RestaurantMenu
    success_url = reverse_lazy('restaurant_app:menu:list')
    form_class = RestaurantMenuForm


class MenuDelete(AuthDeleteView):
    template_name = 'themes/pages/restaurant/menu/menu_confirm_delete.html'
    model = RestaurantMenu
    success_url = reverse_lazy('restaurant_app:menu:list')
