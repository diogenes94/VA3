# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acessar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HoraChegada', models.DateTimeField(verbose_name=b'Hora de Chegada')),
                ('HoraSaida', models.DateTimeField(verbose_name=b'Hora de Sa\xc3\xadda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Local:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NivelAcesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nivel', models.CharField(max_length=30, null=True, verbose_name=b'Nivel de Acesso:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF')),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email')),
                ('Logradouro', models.CharField(max_length=100, null=True, verbose_name=b'Logradouro')),
                ('Numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('UF', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[(b'AC', b'Acre - AC'), (b'AL', b'Alagoas - AL'), (b'AP', b'Amap\xc3\xa1 - AP'), (b'AM', b'Amazonas - AM'), (b'BA', b'Bahia - BA'), (b'CE', b'Cear\xc3\xa1 - CE'), (b'DF', b'Distrito Federal - DF'), (b'ES', b'Esp\xc3\xadrito Santo - ES'), (b'GO', b'Goi\xc3\xa1s - GO'), (b'MA', b'Maranh\xc3\xa3o - MA'), (b'MT', b'Mato Grosso - MT'), (b'MS', b'Mato Grosso do Sul - MS'), (b'MG', b'Minas Gerais - MG'), (b'PA', b'Par\xc3\xa1 - PA'), (b'PB', b'Para\xc3\xadba - PB'), (b'PR', b'Paran\xc3\xa1 - PR'), (b'PE', b'Pernambuco - PE'), (b'PI', b'Piau\xc3\xad - PI'), (b'RJ', b'Rio de Janeiro - RJ'), (b'RN', b'Rio Grande do Norte - RN'), (b'RS', b'Rio Grande do Sul - RS'), (b'RO', b'Rond\xc3\xb4nia - RO'), (b'RR', b'Roraima - RR'), (b'SC', b'Santa Catarina - SC'), (b'SP', b'S\xc3\xa3o Paulo - SP'), (b'SE', b'Sergipe - SE'), (b'TO', b'Tocantins - TO')])),
                ('CEP', models.CharField(max_length=9, null=True, verbose_name=b'CEP')),
                ('URL', models.URLField(null=True, verbose_name=b'P\xc3\xa1gina Pessoal', blank=True)),
                ('NivelAcesso', models.ForeignKey(verbose_name=b'Nivel de Acesso do Usuario', to='Validacao.NivelAcesso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='local',
            name='NivelAcesso',
            field=models.ForeignKey(verbose_name=b'Nivel de Acesso', to='Validacao.NivelAcesso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acessar',
            name='Local',
            field=models.ForeignKey(verbose_name=b'Local de Acesso', to='Validacao.Local'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acessar',
            name='Pessoa',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Validacao.Pessoa'),
            preserve_default=True,
        ),
    ]
