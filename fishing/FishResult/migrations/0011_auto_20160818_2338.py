# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FishResult', '0010_auto_20160818_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish_result',
            name='id',
        ),
        migrations.AddField(
            model_name='fish_result',
            name='result_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
