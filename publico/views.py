from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import ListView
from cadastro.models import Produtos
# Create your views here.

def transparencia(request):
    produtos_list = Produtos.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'transparencia.html', {'produtos_list': produtos_list})

def sugestoes(request):
    return render(request, 'sugestoes.html')

def index(request):
    return render(request, 'publico_index.html')
