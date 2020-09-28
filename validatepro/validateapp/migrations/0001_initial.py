# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-01 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
