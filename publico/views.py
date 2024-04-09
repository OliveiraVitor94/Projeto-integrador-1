from django.http import HttpResponse
from .models import Sugestao
from .forms import SugestaoForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from movimentacao.models import Produto
# Create your views here.

def transparencia(request):
    produtos_list = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'transparencia.html', {'produtos_list': produtos_list})

def criar_sugestao(request):
    if request.method == 'POST':
        form = SugestaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para uma página de sucesso após salvar
    else:
        form = SugestaoForm()
    return render(request, 'sugestao_form.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')




def index(request):
    return render(request, 'publico_index.html')
