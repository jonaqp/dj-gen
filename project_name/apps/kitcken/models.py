from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.reservation.models import Reservation, ReservationMenu
from project_name.apps.user.models import User


class KitchenMenu(models.Model):
    reservation = models.ForeignKey(
        Reservation, verbose_name=_('reservation'),
        related_name="%(app_label)s_%(class)s_reservation")
    cocinero = models.ForeignKey(
        User, verbose_name='cocinero',
        related_name="%(app_label)s_%(class)s_cocinero")
    reservationMenu = models.ForeignKey(
        ReservationMenu, verbose_name=_('reservation menu'),
        related_name="%(app_label)s_%(class)s_reservationMenu")

    class Meta:
        unique_together = ['reservation', 'reservationMenu']

    def __str__(self):
        return self.reservation
