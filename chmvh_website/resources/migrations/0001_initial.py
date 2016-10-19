# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('important', models.BooleanField(default=False, help_text=('categories marked important will be shown at the top of ', 'the resource list'), verbose_name='important')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, verbose_name='address')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='phone number')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('url', models.URLField(blank=True, verbose_name='website URL')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resources.Category', verbose_name='resource category'),
            preserve_default=False,
        ),
    ]