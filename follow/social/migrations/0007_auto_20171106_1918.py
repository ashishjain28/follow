# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20171004_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]