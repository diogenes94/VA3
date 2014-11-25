#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError
import datetime


SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

]
#Não irei usar biblioteca pronta, porque meu choice manual é mais bonito!
ESTADO_OPCOES = [
 ('AC','Acre - AC'),
 ('AL','Alagoas - AL'),
 ('AP','Amapá - AP'),
 ('AM','Amazonas - AM'),
 ('BA','Bahia - BA'),
 ('CE','Ceará - CE'),
 ('DF','Distrito Federal - DF'),
 ('ES','Espírito Santo - ES'),
 ('GO','Goiás - GO'),
 ('MA','Maranhão - MA'),
 ('MT','Mato Grosso - MT'),
 ('MS','Mato Grosso do Sul - MS'),
 ('MG','Minas Gerais - MG'),
 ('PA','Pará - PA'),
 ('PB','Paraíba - PB'),
 ('PR','Paraná - PR'),
 ('PE','Pernambuco - PE'),
 ('PI','Piauí - PI'),
 ('RJ','Rio de Janeiro - RJ'),
 ('RN','Rio Grande do Norte - RN'),
 ('RS','Rio Grande do Sul - RS'),
 ('RO','Rondônia - RO'),
 ('RR','Roraima - RR'),
 ('SC','Santa Catarina - SC'),
 ('SP','São Paulo - SP'),
 ('SE','Sergipe - SE'),
 ('TO','Tocantins - TO')
]

NIVEL_OPCOES = [
(1,'Livre'),
(2,'Restrito'),
(3,'Reservado')
]


class Pessoa(models.Model):
	
	Nome = models.CharField('Nome',max_length=100,null=True)
	NivelAcesso = models.IntegerField('Nivel de Acesso',choices=NIVEL_OPCOES,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=14,unique=True,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=ESTADO_OPCOES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)	
 	URL = models.URLField ('Página Pessoal', max_length=200,null=True,blank=True)
 	
 	def __unicode__(self):
		return self.Nome


class Local(models.Model):
	Nome = models.CharField('Nome do Local:',max_length = 100,null=True)
	NivelAcesso = models.IntegerField('Nivel de Acesso', choices=NIVEL_OPCOES,null=True) 
	
	def __unicode__ (self):
		return self.Nome

	class Meta:
		verbose_name = "Local"
		verbose_name_plural = "Locais"

class Advertencia(models.Model):
	Pessoa = models.ForeignKey(Pessoa,verbose_name='Pessoa')
	Local = models.ForeignKey(Local,verbose_name='Loval')
	Acesso = models.DateTimeField(auto_now=True,null=True)
	Causa = models.CharField('Causa',max_length=30,null=True)

	def __unicode__ (self):
		return "%s - %s - %s" 
	class Meta:
		verbose_name = "Ocorrência"
		verbose_name_plural = "Ocorrências"

class Acessar(models.Model):
	Local = models.ForeignKey(Local, verbose_name='Local de Acesso')
	Pessoa = models.ForeignKey(Pessoa, verbose_name = 'Pessoa')
	HoraChegada = models.DateTimeField('Hora de Chegada',auto_now=True,null=True)
	HoraSaida = models.DateTimeField('Hora de Saída',blank=True,null=True)

	def __unicode__(self):
		return "%s - %s"%(self.Pessoa,self.Local)
	
	def clean(self):

		o = Acessar.objects.filter(Pessoa=self.Pessoa,HoraSaida__isnull=True)
		if o and self.id == None:
			raise ValidationError("Este Usuário Já está em outro local")
		#self.HoraSaida = datetime.datetime.now()

		if self.Local.NivelAcesso > self.Pessoa.NivelAcesso :
			a = Advertencia()
			a.Pessoa = self.Pessoa
			print "Testa"
			a.Local = self.Local
			a.Causa = "Tentativa de acesso em área não permitida"
			a.save()
			raise ValidationError("Este Usuário não possui permissão! Gerando Ocorrência!")

	class Meta:
		verbose_name = "Acesso"
		verbose_name_plural = "Acessos"


	




# Create your models here.