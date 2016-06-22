# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=150, unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='city',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='country',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='line_1',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='line_2',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='line_3',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='postalcode',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='state',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
