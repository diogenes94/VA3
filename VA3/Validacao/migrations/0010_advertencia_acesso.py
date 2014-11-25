# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0009_advertencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertencia',
            name='Acesso',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2014, 11, 25, 17, 30, 31, 412855)),
            preserve_default=True,
        ),
    ]
