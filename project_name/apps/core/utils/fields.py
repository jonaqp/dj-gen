import uuid

from django.conf import settings
from django.db import models
from django.db.models import ForeignKey
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.middleware.current_user import UserMiddleware
from project_name.apps.core.utils.funct_dates import str_datetime
from ..constants import SELECT_DEFAULT, STATUS_MODEL1, ENABLED
from ..queryset import AuditableManager

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CurrentUserField(ForeignKey):
    def __init__(self, to_field=None, to=AUTH_USER_MODEL, **kwargs):
        self.add_only = kwargs.pop('add_only', False)
        kwargs.update({
            'editable': False,
            'null': True,
            'to': to,
            'to_field': to_field,
        })
        super().__init__(**kwargs)

    def pre_save(self, model_instance, add):
        if add or not self.add_only:
            user = UserMiddleware.get_user()
            if user:
                setattr(model_instance, self.attname, user.pk)
                return user.pk
        return super().pre_save(model_instance, add)


class TimeStampedModel(models.Model):
    date_created = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now_add=True,
        verbose_name=_('date created'))
    date_modified = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now=True,
        verbose_name=_('date modified'))
    created_by = CurrentUserField(
        add_only=True, related_name="%(app_label)s_%(class)s_created_by",)
    modified_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_modified_by")

    def save(self, *args, **kwargs):
        if self.pk:
            self.date_modified = str_datetime()
        else:
            self.date_created = str_datetime()
            kwargs['force_insert'] = False
        return super().save(*args, **kwargs)

    def delete(self, force=False, *args, **kwargs):
        self.is_deleted = True
        self.save()
        if force:
            return super().delete(*args, **kwargs)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    uid = models.UUIDField(editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    is_deleted = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True


class StatusCurrent(models.Model):
    current_status = models.CharField(
        max_length=10, choices=SELECT_DEFAULT + STATUS_MODEL1, default=ENABLED)

    class Meta:
        abstract = True


class ManagerBase(models.Model):
    current = AuditableManager()
    objects = models.Manager()

    class Meta:
        abstract = True


class BaseModel(ManagerBase, TimeStampedModel, StatusModel):
    class Meta:
        abstract = True


class BaseModel2(ManagerBase, UUIDModel, TimeStampedModel, StatusModel):
    class Meta:
        abstract = True
