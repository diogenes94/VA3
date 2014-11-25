# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0012_remove_advertencia_acesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertencia',
            name='Acesso',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
