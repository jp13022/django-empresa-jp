from django.contrib import admin
from .models import Funcionarios, MensagemContato, Produtos, Clientes

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'departamento', 'data_contratacao', 'status')
    search_fields = ('nome',)
    list_filter = ('status', 'data_contratacao')


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ('lido', 'data_envio')


@admin.register(Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'categoria')
    list_filter = ('em_estoque', 'valor', 'categoria')

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'tel')