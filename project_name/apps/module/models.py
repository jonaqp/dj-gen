from django.db import models

from project_name.apps.core.models import Role, Permission
from project_name.apps.core.utils.fields import BaseModel


class Module(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    match = models.CharField(
        default="#", max_length=200, null=False, blank=False)
    reference = models.CharField(
        unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']
        unique_together = ['name']
        verbose_name_plural = "1. Modules"

    def __str__(self):
        return self.name


class ModuleItem(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    match = models.CharField(
        default="#", max_length=200, null=False, blank=False)
    reference = models.CharField(
        unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False, default=0)
    module = models.ForeignKey(Module)

    def module_text(self):
        return "{0}".format(self.module)

    class Meta:
        ordering = ['module']
        verbose_name_plural = "2. Module Items"

    def __str__(self):
        return "{0}-{1}".format(self.module, self.name)


class RoleModule(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,
                             blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL,
                               blank=True, null=True)

    class Meta:
        unique_together = ['module']
        verbose_name_plural = "3. Module Teams"

    # def get_team_list(self):
    #     return ", ".join([p.name for p in self.role.objects.all()])

    def get_moduleitem_list(self):
        module_item = RoleModuleItem.objects.filter(role_module=self)
        return ", ".join([p.moduleitem.name for p in module_item])

    def __str__(self):
        return "{0}".format(self.module)


class RoleModuleItem(BaseModel):
    role_module = models.ForeignKey(RoleModule)
    moduleitem = models.ForeignKey(ModuleItem)
    permission = models.ManyToManyField(Permission, blank=True)

    class Meta:
        unique_together = ['role_module', 'moduleitem']
        verbose_name_plural = "4. Module Item Teams"

    def __str__(self):
        return "{0} | {1}".format(self.role_module, self.moduleitem.name)
