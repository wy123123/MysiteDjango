# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20150824_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('regionid', models.IntegerField(serialize=False, primary_key=True, db_column=b'RegionID')),
                ('regiondescription', models.TextField(db_column=b'RegionDescription')),
            ],
            options={
                'db_table': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('shipperid', models.IntegerField(serialize=False, primary_key=True, db_column=b'ShipperID')),
                ('companyname', models.TextField(db_column=b'CompanyName')),
                ('phone', models.TextField(null=True, db_column=b'Phone', blank=True)),
            ],
            options={
                'db_table': 'Shippers',
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplierid', models.IntegerField(serialize=False, primary_key=True, db_column=b'SupplierID')),
                ('companyname', models.TextField(db_column=b'CompanyName')),
                ('contactname', models.TextField(null=True, db_column=b'ContactName', blank=True)),
                ('contacttitle', models.TextField(null=True, db_column=b'ContactTitle', blank=True)),
                ('address', models.TextField(null=True, db_column=b'Address', blank=True)),
                ('city', models.TextField(null=True, db_column=b'City', blank=True)),
                ('region', models.TextField(null=True, db_column=b'Region', blank=True)),
                ('postalcode', models.TextField(null=True, db_column=b'PostalCode', blank=True)),
                ('country', models.TextField(null=True, db_column=b'Country', blank=True)),
                ('phone', models.TextField(null=True, db_column=b'Phone', blank=True)),
                ('fax', models.TextField(null=True, db_column=b'Fax', blank=True)),
                ('homepage', models.TextField(null=True, db_column=b'HomePage', blank=True)),
            ],
            options={
                'db_table': 'Suppliers',
            },
        ),
    ]
