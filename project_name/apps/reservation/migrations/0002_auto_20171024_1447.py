# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_reservation_guest1', to=settings.AUTH_USER_MODEL, verbose_name='guest1'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest2',
            field=models.CharField(max_length=100, verbose_name='guest2'),
        ),
    ]