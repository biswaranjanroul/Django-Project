# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-22 19:29
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enquryformapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquarydata',
            name='course',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('PY', 'Python'), ('DJ', 'Django'), ('RA', 'Rest API')], max_length=100),
        ),
    ]
