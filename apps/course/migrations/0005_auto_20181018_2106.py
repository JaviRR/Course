# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-18 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_delete_validator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='course.Course'),
        ),
    ]
