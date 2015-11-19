# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(null=True, blank=True, max_length=255)),
                ('address_2', models.CharField(null=True, blank=True, max_length=255)),
                ('city', models.CharField(null=True, blank=True, max_length=30)),
                ('state', models.CharField(null=True, blank=True, max_length=10)),
                ('zip', models.CharField(null=True, blank=True, max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
