from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.restaurant.models import Restaurant, RestaurantMenu, RestaurantTable
from project_name.apps.user.models import User


class Reservation(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, verbose_name=_('restaurant'),
        related_name="%(app_label)s_%(class)s_restaurant")
    mozo = models.ForeignKey(
        User, verbose_name=_('mozo'),
        related_name="%(app_label)s_%(class)s_mozo")
    guest1 = models.ForeignKey(
        User, verbose_name=_('guest1'), blank=True, null=True,
        related_name="%(app_label)s_%(class)s_guest1")
    guest2 = models.CharField(
        _('guest2'), max_length=100, blank=False, null=False)
    person_total = models.IntegerField(default=1)
    dateReservation = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_('date reservation'))
    is_confirmed = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return "Reservation {0}".format(self.id)


class ReservationTable(models.Model):
    reservation = models.ForeignKey(
        Reservation, verbose_name=_('reservation'),
        related_name="%(app_label)s_%(class)s_reservation")
    restaurantTable = models.ForeignKey(
        RestaurantTable, verbose_name=_('restaurant table'),
        related_name="%(app_label)s_%(class)s_restaurantTable")

    class Meta:
        unique_together = ['reservation', 'restaurantTable']

    def __str__(self):
        return "Reservation {0}".format(self.reservation.id)


class ReservationMenu(models.Model):
    reservation = models.ForeignKey(
        Reservation, verbose_name=_('reservation'),
        related_name="%(app_label)s_%(class)s_reservation")
    restaurantMenu = models.ForeignKey(
        RestaurantMenu, verbose_name=_('restaurant menu'),
        related_name="%(app_label)s_%(class)s_restaurantMenu")
    is_kitchen_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['reservation', 'restaurantMenu']

    def __str__(self):
        return "Reservation {0}".format(self.reservation.id)
