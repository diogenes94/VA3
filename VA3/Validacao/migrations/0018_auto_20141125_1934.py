# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0017_auto_20141125_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='NivelAcesso',
            field=models.IntegerField(null=True, verbose_name=b'Nivel de Acesso', choices=[(1, b'Livre'), (2, b'Restrito'), (3, b'Reservado')]),
        ),
    ]
