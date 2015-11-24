# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas_list', '0002_auto_20151120_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_funded',
            field=models.BooleanField(default=False),
        ),
    ]
