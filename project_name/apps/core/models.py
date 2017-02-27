from django.db import models
from django.utils.translation import ugettext_lazy as _

from .manager import TeamManager, PermissionManager
from .utils.fields import BaseModel2


class Team(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)

    objects = TeamManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class Role(BaseModel2):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,
                             blank=True, null=True)
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    class Meta:
        unique_together = ('team', 'name', 'codename',)
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return "{0}:{1}".format(str(self.team.name), str(self.codename))

    def natural_key(self):
        return (self.name,)


class RoleTeam(BaseModel2):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,
                             blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,
                             blank=True, null=True)

    class Meta:
        unique_together = ('role', 'team',)
        verbose_name = _('Role Group', )
        verbose_name_plural = _('Role Groups', )

    def __str__(self):
        return "{0}:{1}".format(str(self.team.name), str(self.role.codename))


class Permission(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    objects = PermissionManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
