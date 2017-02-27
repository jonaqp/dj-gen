# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 11:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import project_name.apps.core.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_team_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='modified_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_team_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='role',
            name='created_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_role_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='role',
            name='modified_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_role_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]