# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_permission'),
        ('module', '0004_auto_20170106_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduleitemteam',
            name='permission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Permission'),
        ),
        migrations.AlterField(
            model_name='moduleteam',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='module.Module'),
        ),
    ]
