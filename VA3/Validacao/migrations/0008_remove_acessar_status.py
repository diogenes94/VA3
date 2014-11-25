# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0007_auto_20141125_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acessar',
            name='status',
        ),
    ]
