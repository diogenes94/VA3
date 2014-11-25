# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0006_nivelacesso_peso'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acessar',
            unique_together=None,
        ),
    ]
