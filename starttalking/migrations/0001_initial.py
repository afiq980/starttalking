# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-31 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('nsfw', models.BooleanField(default=False)),
            ],
        ),
    ]
