from django.contrib import admin

from .models import Team, Role


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
