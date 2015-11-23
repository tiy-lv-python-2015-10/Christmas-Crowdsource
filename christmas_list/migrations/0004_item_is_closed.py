# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas_list', '0003_item_is_funded'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
