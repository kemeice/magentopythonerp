# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0005_remove_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Websites',
        ),
        migrations.AddField(
            model_name='product',
            name='Color',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Horeca',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Meubis_be_France',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Meubis_be_Nederlands',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Meubis_nl_Nederlads',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='groups',
            field=models.CharField(verbose_name='Websites', choices=[('Default', 'Default'), ('Beds', 'Beds')], default='Please select', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(null=True, blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='lenght',
            field=models.CharField(null=True, blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(null=True, blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(null=True, blank=True, max_length=120),
        ),
    ]
