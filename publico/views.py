from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def transparencia(request):
    return render(request, 'transparencia.html')

def lista_produtos(request):
    return render(request, 'lista_produtos.html')

def index(request):
    return render(request, 'publico_index.html')