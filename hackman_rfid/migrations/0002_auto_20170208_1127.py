# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackman_rfid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfidcard',
            name='revoked',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='rfidcard',
            name='rfid_hash',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='rfidlog',
            name='time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
