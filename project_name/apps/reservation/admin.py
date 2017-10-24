from django.contrib import admin

from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReservationTable)
class ReservationTableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReservationMenu)
class ReservationMenuAdmin(admin.ModelAdmin):
    pass
