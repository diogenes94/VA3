# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0011_auto_20141125_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertencia',
            name='Acesso',
        ),
    ]
