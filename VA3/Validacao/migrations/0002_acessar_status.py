# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessar',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'Situa\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
    ]
