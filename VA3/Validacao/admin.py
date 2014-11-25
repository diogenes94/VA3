from django.contrib import admin
from models import NivelAcesso,Pessoa,Local,Acessar, Advertencia

class NivelAcessoAdmin(admin.ModelAdmin):
	
	list_display = ['Nivel']
	list_filter = ['Nivel']
	search_fields = ['Nivel']
	save_as = True


class PessoaAdmin(admin.ModelAdmin):

	list_display = ['Nome','NivelAcesso','Sexo','CPF','Email']
	list_filter = ['Nome','NivelAcesso','Sexo','CPF','Email']
	search_fields = ['Nome','NivelAcesso','CPF','Email']
	save_as = True

class LocalAdmin(admin.ModelAdmin):

	list_display = ['Nome','NivelAcesso']
	list_filter = ['Nome','NivelAcesso']
	search_fields = ['Nome','NivelAcesso']
	save_as = True

class AcessarAdmin(admin.ModelAdmin):
	
	list_display = ['Local','Pessoa','HoraChegada','HoraSaida']
	list_filter = ['Local','Pessoa','HoraChegada','HoraSaida']
	search_fields = ['Local','Pessoa']
	save_as = True
class AdvertenciaAdmin(admin.ModelAdmin):

	list_display = ['Pessoa','Local','Acesso','Causa']
	list_filter = ['Pessoa','Local']
	search_fields = ['Pessoa','Local']
	save_as = True

# Register your models here.
admin.site.register(NivelAcesso,NivelAcessoAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Local,LocalAdmin)
admin.site.register(Acessar,AcessarAdmin)
admin.site.register(Advertencia, AdvertenciaAdmin)
