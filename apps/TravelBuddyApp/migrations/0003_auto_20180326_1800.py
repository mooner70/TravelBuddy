# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBuddyApp', '0002_remove_travelplans_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelplans',
            old_name='travel_end_date',
            new_name='travel_date_from',
        ),
        migrations.RenameField(
            model_name='travelplans',
            old_name='travel_start_date',
            new_name='travel_date_to',
        ),
    ]