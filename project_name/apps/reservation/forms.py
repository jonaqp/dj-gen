from django import forms

from project_name.apps.restaurant.models import RestaurantTable
from project_name.apps.user.models import User
from .models import (
    Reservation, ReservationMenu, ReservationTable
)


class ReservationForm(forms.ModelForm):
    mozo = forms.ModelChoiceField(
        queryset=User.objects.all(), required=True)
    guest1 = forms.ModelChoiceField(
        queryset=User.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mozo'].queryset = User.objects.filter(team__id=1)

        self.fields['guest1'].queryset = User.objects.filter(team__id=5)
        self.fields['guest1'].required = False

    class Meta:
        model = Reservation
        fields = ["restaurant", "mozo", "guest1", "guest2",
                  "person_total", "dateReservation", "is_confirmed", "is_finished"]


class ReservationMenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurantMenu'].widget.attrs.update(
            {'class': 'form-control cls_restaurant_menu'})
        self.fields['is_kitchen_completed'].widget.attrs.update(
            {'class': 'form-control cls_restaurant_kitchen styled cls_chk'})

    class Meta:
        model = ReservationMenu
        fields = ["restaurantMenu", "is_kitchen_completed"]

    def save(self, reservation=None, *args, **kwargs):
        menu = super().save(*args, **kwargs)
        if reservation:
            menu.reservation = reservation
        menu.save()
        return menu


class ReservationTableForm(forms.ModelForm):
    restaurantTable = forms.ModelChoiceField(
        queryset=RestaurantTable.objects.filter(is_occupied=False), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            _id = list()
            table = self.instance.restaurantTable.id
            filter = RestaurantTable.objects.filter(pk=table).values_list('id', flat=True)
            for f in filter:
                _id.append(f)
            filter2 = RestaurantTable.objects.filter(is_occupied=False).values_list('id', flat=True)
            for f in filter2:
                _id.append(f)
            self.fields['restaurantTable'].queryset = RestaurantTable.objects.filter(id__in=_id)

    class Meta:
        model = ReservationTable
        fields = ["restaurantTable"]

    def save(self, reservation=None, *args, **kwargs):
        table = super().save(*args, **kwargs)
        if reservation:
            table.reservation = reservation
        table.save()
        return table
