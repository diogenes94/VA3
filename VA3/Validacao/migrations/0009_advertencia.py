# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Validacao', '0008_remove_acessar_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Local', models.ForeignKey(verbose_name=b'Loval', to='Validacao.Local')),
                ('Pessoa', models.ForeignKey(verbose_name=b'Pessoa', to='Validacao.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
