# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("title",),
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="resource",
            options={"ordering": ("title",)},
        ),
    ]
