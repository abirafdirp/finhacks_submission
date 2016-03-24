# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20160323_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store'),
        ),
    ]