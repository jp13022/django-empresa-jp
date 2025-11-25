from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ContatoModelForm, CarrinhoModelForm



def home(request):
    return render(request, "home.html")


def produtos(request):
    produtos = Produtos.objects.filter(em_estoque=True)
    context = {"produtos": produtos}
    return render(request, 'produtos.html', context)


def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    else:
        form = ContatoModelForm()

    return render(request, 'contato/contatos.html', {'form': form})


def clientes(request):
    if request.method == 'POST':
        form = CarrinhoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra_efetuada')
    else:
        form = CarrinhoModelForm()

    return render(request, 'cadastro/carrinho.html', {'form': form})


def compra_efetuada_view(request):
    return render(request, 'cadastro/compra_efetuada.html')


def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')
