# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FishResult', '0004_auto_20160814_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_master',
            name='maker_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='FishResult.maker_master', verbose_name='メーカーID'),
        ),
    ]
