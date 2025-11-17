from django.shortcuts import redirect, render
from .models import Funcionarios
from .forms import ContatoModelForm, ClientesModelForm
from .models import Produtos
from .models import Clientes

# Create your views here.
def home(request):
    return render(request,'home.html')

def produtos(request):
    produtos = Produtos.objects.filter(em_estoque=True)
    context = {
        "produtos": produtos
    }
    return render(request,'produtos.html', context)

def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)


# ----------------------------------------
# FORMULÁRIO DE CONTATO (NÃO MEXI)
# ----------------------------------------

def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    
    else:
        form = ContatoModelForm()

    return render(request, 'contato/contatos.html', {'form': form})


# ----------------------------------------
# ✅ FORMULÁRIO DE CLIENTES (CORRIGIDO)
# ----------------------------------------

# ----------------------------------------
# FORMULÁRIO DE CLIENTES (CORRIGIDO)
# ----------------------------------------

def clientes(request):
    if request.method == 'POST':
        form = ClientesModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_sucesso')  # redireciona para a página correta
    else:
        form = ClientesModelForm()

    return render(request, 'cadastro/clientes.html', {'form': form})


def cliente_sucesso_view(request):
    return render(request, 'cadastro/cliente_sucesso.html')


# ----------------------------------------
# OUTRAS VIEWS (NÃO MEXI)
# ----------------------------------------

def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')

