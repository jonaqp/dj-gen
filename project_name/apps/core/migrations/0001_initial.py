# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 11:04
from __future__ import unicode_literals

import uuid

from django.db import migrations, models

import project_name.apps.core.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('codename', models.CharField(max_length=80, unique=True, verbose_name='codename')),
            ],
            options={
                'verbose_name_plural': 'roles',
                'verbose_name': 'role',
            },
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
            ],
            options={
                'verbose_name_plural': 'groups',
                'verbose_name': 'group',
            },
            managers=[
                ('objects', project_name.apps.core.manager.TeamManager()),
            ],
        ),
    ]