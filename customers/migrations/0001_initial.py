# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_1', models.CharField(max_length=300)),
                ('line_2', models.CharField(max_length=300)),
                ('line_3', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=150)),
                ('postalcode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(to='customers.CustomerAddress'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
