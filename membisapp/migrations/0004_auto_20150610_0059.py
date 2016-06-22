# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meubisapp', '0003_auto_20150526_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Websites',
            field=models.CharField(verbose_name='Websites', max_length=50, default='Please select', choices=[('Meubis.be_Nederlands', 'Nederlands'), ('Meubis.be_France', 'France'), ('Meubis.nl_Nederlads', 'nl_Nederlads'), ('Horeca', 'Horeca')]),
        ),
        migrations.AddField(
            model_name='product',
            name='advantage_1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='advantage_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='advantage_3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.CharField(verbose_name='Delivery time', max_length=50, default='Please select', choices=[('3day', 'Three Days'), ('7days', 'Seven Days'), ('14days', 'Fourteen Days'), ('21 Days', 'Twenty One Days')]),
        ),
        migrations.AddField(
            model_name='product',
            name='order_per_X',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shortdescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_delivery_time',
            field=models.CharField(max_length=10, default=7),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_sku',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=10, default=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.CharField(verbose_name='Product type', max_length=50, default='simple', choices=[('simple', 'Simple'), ('configurable', 'Configurable'), ('grouped', 'Grouped'), ('bundle', 'Bundle')]),
        ),
    ]
