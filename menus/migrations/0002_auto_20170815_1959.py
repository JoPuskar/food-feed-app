# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='retaurants',
            new_name='restaurants',
        ),
    ]
