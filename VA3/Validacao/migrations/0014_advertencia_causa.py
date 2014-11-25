# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0013_advertencia_acesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertencia',
            name='Causa',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Causa'),
            preserve_default=True,
        ),
    ]
