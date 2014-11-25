# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0018_auto_20141125_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessar',
            options={'verbose_name': 'Acesso', 'verbose_name_plural': 'Acessos'},
        ),
        migrations.AlterModelOptions(
            name='advertencia',
            options={'verbose_name': 'Ocorr\xeancia', 'verbose_name_plural': 'Ocorr\xeancias'},
        ),
    ]
