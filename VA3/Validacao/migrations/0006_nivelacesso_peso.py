# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0005_auto_20141124_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='nivelacesso',
            name='Peso',
            field=models.IntegerField(null=True, verbose_name=b'Peso'),
            preserve_default=True,
        ),
    ]
