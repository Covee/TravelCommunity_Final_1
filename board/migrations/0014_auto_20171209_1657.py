# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_merge_20171108_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='upload/%Y/%m/%d/video'),
        ),
        migrations.AlterField(
            model_name='post',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
