# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170712_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='street_number',
        ),
    ]
