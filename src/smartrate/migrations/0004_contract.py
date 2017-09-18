# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartrate', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=5)),
                ('base_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pay_freq', models.CharField(max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartrate.Customer')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartrate.Hotel')),
            ],
        ),
    ]
