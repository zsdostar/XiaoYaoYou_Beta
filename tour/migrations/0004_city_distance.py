# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-17 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='distance',
            field=models.FloatField(default=0.0, verbose_name='\u4e34\u65f6\u8ddd\u79bb'),
        ),
    ]