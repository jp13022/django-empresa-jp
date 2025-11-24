from django.contrib import admin
from .models import MensagemContato, Produtos, Carrinhos

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ('lido', 'data_envio')


@admin.register(Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'categoria')
    list_filter = ('em_estoque', 'valor', 'categoria')

@admin.register(Carrinhos)
class CarrinhosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'tel')