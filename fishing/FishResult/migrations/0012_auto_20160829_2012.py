# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FishResult', '0011_auto_20160818_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish_result',
            name='latitude',
            field=models.FloatField(verbose_name='緯度(地図をクリック)'),
        ),
        migrations.AlterField(
            model_name='fish_result',
            name='longitude',
            field=models.FloatField(verbose_name='経度(地図をクリック)'),
        ),
        migrations.AlterField(
            model_name='fish_result',
            name='result_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='釣果ID'),
        ),
    ]