# Register your models here.
from django.contrib import admin

from .models import (
    Module, ModuleItem, ModuleTeam, ModuleItemTeam
)


class ModuleItemAdminInline(admin.TabularInline):
    model = ModuleItem


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ModuleItemAdminInline]


class ModuleItemTeamAdminInline(admin.TabularInline):
    list_display = ['module_team', 'moduleitem']
    model = ModuleItemTeam
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        print(db_field.name)
        if db_field.name == "moduleitem":
            if request._obj is not None:
                pass
                field.queryset = ModuleItem.objects.filter(module=request._obj.module)
            else:
                field.queryset = field.queryset.none()
        return field


@admin.register(ModuleTeam)
class ModuleTeamAdmin(admin.ModelAdmin):
    list_display = ['module', 'get_team_list', 'get_moduleitem_list']
    inlines = [ModuleItemTeamAdminInline]

    def get_form(self, request, obj=None, **kwargs):
        request._obj = obj
        return super().get_form(request, obj, **kwargs)
