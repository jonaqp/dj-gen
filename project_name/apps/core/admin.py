from django.contrib import admin

from .models import Team, Role, RoleTeam, Permission


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(RoleTeam)
class RoleTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass
