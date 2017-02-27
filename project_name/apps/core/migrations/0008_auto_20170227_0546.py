# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 05:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170227_0423'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roleteam',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='roleteam',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='roleteam',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='roleteam',
            name='role',
        ),
        migrations.RemoveField(
            model_name='roleteam',
            name='team',
        ),
        migrations.DeleteModel(
            name='RoleTeam',
        ),
    ]
