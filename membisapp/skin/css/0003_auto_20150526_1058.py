# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0002_auto_20150526_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.CharField(verbose_name='Product type', choices=[('simple', 'Simple'), ('configurable', 'Configurable'), ('grouped', 'Grouped'), ('bundle', 'Bundle')], max_length=50),
        ),
    ]
