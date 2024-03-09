from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def colaboradores(request):
    return render(request, 'colaboradores.html')

def produtos(request):
    return render(request, 'produtos.html')