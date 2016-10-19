# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deceased', models.BooleanField(default=False, help_text="Patients marked as deceased will have their picture displayed in the 'In Memoriam' section.", verbose_name='deceased')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, help_text='This is only used to identify the patient, and is not displayed publicly.', max_length=100, verbose_name='last name')),
                ('picture', models.ImageField(height_field='picture_height', upload_to=gallery.models.patient_image_path, verbose_name='picture', width_field='picture_width')),
            ],
        ),
    ]