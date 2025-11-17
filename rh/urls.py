from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('clientes/', views.clientes, name='clientes'),

    # NOVA ROTA — página de sucesso do cliente
    path('clientes/sucesso/', views.cliente_sucesso_view, name='cliente_sucesso'),

    path('funcionarios/', views.funcionarios, name='funcionarios'),

    # Contatos
    path('contato/', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]
