from django.db import models
from django.utils.translation import ugettext_lazy as _

from .manager import TeamManager, RoleManager, PermissionManager
from .utils.fields import BaseModel2


class Team(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)

    objects = TeamManager()

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class Role(BaseModel2):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,
                             blank=True, null=True)
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    objects = RoleManager()

    class Meta:
        unique_together = ('team', 'codename')
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class Permission(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    objects = RoleManager()

    class Meta:
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
