# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBuddyApp', '0003_auto_20180326_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplans',
            name='travel_date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travelplans',
            name='travel_date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
