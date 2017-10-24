from django.contrib import admin

from . import models


@admin.register(models.KitchenMenu)
class KitchenMenuAdmin(admin.ModelAdmin):
    pass
