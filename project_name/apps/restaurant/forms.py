from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import (
    Restaurant, RestaurantMenu, RestaurantTable
)


class RestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['codigo'].widget.attrs.update(
        #     {'placeholder': _('Code'), 'required': True,
        #      'class': 'form-control'})
        # self.fields['nombre'].widget.attrs.update(
        #     {'placeholder': _('Name'), 'required': True,
        #      'class': 'form-control'})

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantMenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['codigo'].widget.attrs.update(
        #     {'placeholder': _('Code'), 'required': True,
        #      'class': 'form-control'})
        # self.fields['nombre'].widget.attrs.update(
        #     {'placeholder': _('Name'), 'required': True,
        #      'class': 'form-control'})

    class Meta:
        model = RestaurantMenu
        fields = "__all__"


class RestaurantTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['codigo'].widget.attrs.update(
        #     {'placeholder': _('Code'), 'required': True,
        #      'class': 'form-control'})
        # self.fields['nombre'].widget.attrs.update(
        #     {'placeholder': _('Name'), 'required': True,
        #      'class': 'form-control'})

    class Meta:
        model = RestaurantTable
        fields = "__all__"
