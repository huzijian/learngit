# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-17 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='Time',
            field=models.IntegerField(default=1),
        ),
    ]
