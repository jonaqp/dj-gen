from django.forms import inlineformset_factory

from .forms import (
    ReservationMenuForm
)
from .models import (
    Reservation, ReservationMenu
)

ReservationMenuFormSet = inlineformset_factory(
    Reservation, ReservationMenu, form=ReservationMenuForm,
    extra=0, can_delete=True
)
