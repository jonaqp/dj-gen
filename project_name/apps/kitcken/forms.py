from django import forms

from project_name.apps.restaurant.models import RestaurantMenu
from .models import (
    ReservationMenu
)


class ReservationMenuForm(forms.ModelForm):
    restaurantMenu = forms.ModelChoiceField(empty_label=None,
        queryset=RestaurantMenu.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurantMenu'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['is_kitchen_completed'].widget.attrs.update(
            {'class': 'form-control styled cls_chk'})

        if self.instance.id:
            _menu = self.instance.restaurantMenu.id
            self.fields['restaurantMenu'].queryset = RestaurantMenu.objects.filter(pk=_menu)

    class Meta:
        model = ReservationMenu
        fields = ["restaurantMenu", "is_kitchen_completed"]

    def save(self, reservation=None, *args, **kwargs):
        menu = super().save(*args, **kwargs)
        if reservation:
            menu.reservation = reservation
        menu.save()
        return menu
