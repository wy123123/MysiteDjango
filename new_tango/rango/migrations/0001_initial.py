# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, db_column='Name')),
                ('price', models.TextField(null=True, db_column='Price', blank=True)),
                ('time', models.DateField(null=True, db_column='Time', blank=True)),
            ],
            options={
                'db_table': 'asos',
            },
        ),
        migrations.CreateModel(
            name='F21',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, db_column='Name', blank=True)),
                ('price', models.TextField(null=True, db_column='Price', blank=True)),
                ('time', models.DateField(null=True, db_column='Time', blank=True)),
            ],
            options={
                'db_table': 'f21',
            },
        ),
        migrations.CreateModel(
            name='Topshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, blank=True)),
                ('price', models.TextField(null=True, blank=True)),
                ('time', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'topshop',
            },
        ),
        migrations.CreateModel(
            name='Zara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, blank=True)),
                ('price', models.TextField(null=True, blank=True)),
                ('time', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'zara',
            },
        ),
    ]
