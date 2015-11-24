# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='charge_id',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pledge',
            name='is_refunded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
