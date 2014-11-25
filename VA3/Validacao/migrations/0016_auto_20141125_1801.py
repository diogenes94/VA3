# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0015_auto_20141125_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessar',
            name='HoraSaida',
            field=models.DateTimeField(null=True, verbose_name=b'Hora de Sa\xc3\xadda', blank=True),
        ),
    ]
