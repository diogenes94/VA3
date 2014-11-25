# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0014_advertencia_causa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessar',
            name='HoraChegada',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Hora de Chegada', null=True),
        ),
        migrations.AlterField(
            model_name='acessar',
            name='HoraSaida',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Hora de Sa\xc3\xadda', null=True),
        ),
    ]
