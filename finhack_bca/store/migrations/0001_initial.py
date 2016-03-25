# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.IntegerField(default=0)),
                ('domain', models.URLField()),
                ('short_description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Toko',
                'verbose_name': 'Toko',
                'permissions': (('view_store', 'View store'),),
            },
        ),
    ]
