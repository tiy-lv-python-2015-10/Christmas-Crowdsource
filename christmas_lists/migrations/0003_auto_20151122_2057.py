# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas_lists', '0002_auto_20151122_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='charge_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
