# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 23:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_auto_20160323_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countertopup',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counter_top_ups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customertopup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_ups', to=settings.AUTH_USER_MODEL),
        ),
    ]
