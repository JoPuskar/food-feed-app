# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20170815_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
