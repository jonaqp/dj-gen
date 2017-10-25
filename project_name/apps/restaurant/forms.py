from django import forms

from .models import (
    Restaurant, RestaurantMenu, RestaurantTable
)


class RestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantMenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = RestaurantMenu
        fields = "__all__"


class RestaurantTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = RestaurantTable
        fields = "__all__"
