from django.contrib import admin

from . import models


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RestaurantMenu)
class RestaurantMenuAdmin(admin.ModelAdmin):
    pass
