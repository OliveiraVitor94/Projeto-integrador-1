from django.shortcuts import render
from .forms import ProdutosForm
from django.views.generic import ListView
from .models import Produtos

def colaboradores(request):
    return render(request, 'colaboradores.html')

def produtos(request):
    produtos_list = Produtos.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'produtos.html', {'produtos_list': produtos_list})

def cadastro(request):
    return render(request, 'cadastro.html')


