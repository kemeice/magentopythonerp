# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0003_auto_20150526_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.CharField(choices=[('simple', 'Simple'), ('configurable', 'Configurable'), ('grouped', 'Grouped'), ('bundle', 'Bundle')], default='simple', max_length=50, verbose_name='Product type'),
        ),
    ]
