# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 03:24
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models

import project_name.apps.core.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='name')),
                ('code_name', models.CharField(max_length=80, unique=True, verbose_name='name')),
                ('created_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_role_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_role_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='name')),
                ('created_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_team_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_team_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
    ]
