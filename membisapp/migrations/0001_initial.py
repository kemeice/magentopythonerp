# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('catalog', models.ForeignKey(related_name='categories', to='meubisapp.Catalog')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='meubisapp.CatalogCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(max_digits=100, decimal_places=2, default=0.0)),
                ('sale_price', models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(related_name='products', to='meubisapp.CatalogCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('attribute', models.ForeignKey(to='meubisapp.ProductAttribute')),
                ('product', models.ForeignKey(related_name='details', to='meubisapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='products/images/')),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='meubisapp.Product')),
            ],
        ),
    ]
