# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mageconnect',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('storeurl', models.TextField(blank=True)),
                ('key', models.TextField(blank=True)),
                ('user', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type_product',
            field=models.CharField(default=datetime.datetime(2015, 5, 26, 15, 54, 11, 10095, tzinfo=utc), choices=[('simple', 'Simple'), ('configurable', 'Configurable'), ('grouped', 'Grouped'), ('bundle', 'Bundle')], verbose_name='Product type'),
            preserve_default=False,
        ),
    ]
