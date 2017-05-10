# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-10 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_auto_20170510_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='wait_for',
            field=models.SmallIntegerField(choices=[(0, 'Ok'), (1, 'Disk'), (2, 'Memory'), (3, 'CPU'), (4, 'Former'), (5, 'Peer'), (6, 'Virtual Memory')], default=0),
        ),
    ]
