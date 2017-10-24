from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.utils.upload_folder import upload_restaurant_menu


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100, blank=False, null=False)
    description = models.TextField()
    address = models.CharField(
        max_length=100, blank=True, null=True)
    is_ready = models.BooleanField(default=False)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class RestaurantMenu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, verbose_name=_('restaurant'),
        related_name="%(app_label)s_%(class)s_restaurant")
    name = models.CharField(
        max_length=100, blank=False, null=False)
    file = models.FileField(
        _("file"), upload_to=upload_restaurant_menu, blank=False, null=False)
    description = models.TextField()
    amount = models.DecimalField(
        _("amount"), max_digits=8, decimal_places=2, default=0)

    class Meta:
        unique_together = ['restaurant', 'name']

    def __str__(self):
        return self.name


class RestaurantTable(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, verbose_name=_('restaurant'),
        related_name="%(app_label)s_%(class)s_restaurant")
    position = models.IntegerField(default=0)
    count_table = models.IntegerField(default=0)
    is_occupied = models.BooleanField(default=False)

    class Meta:
        unique_together = ['position', 'restaurant']

    def __str__(self):
        return self.position
