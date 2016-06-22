# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0004_auto_20150610_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
