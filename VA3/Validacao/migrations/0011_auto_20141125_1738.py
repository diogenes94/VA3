# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0010_advertencia_acesso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertencia',
            name='Acesso',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
