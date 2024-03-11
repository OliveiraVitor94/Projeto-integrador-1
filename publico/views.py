from django.http import HttpResponse
from .models import Sugestao
from .forms import SugestaoForm
from django.shortcuts import render
from django.views.generic import ListView
from movimentacao.models import Produtos
# Create your views here.

def transparencia(request):
    produtos_list = Produtos.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'transparencia.html', {'produtos_list': produtos_list})

def sugestoes(request):
    mensagem = None
    form = SugestaoForm()  # Criar o formulário mesmo em caso de requisição GET

    if request.method == 'POST':
        form = SugestaoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem = "Sugestão enviada com sucesso!"
            form = SugestaoForm()  # Resetar o formulário após o envio

    return render(request, 'sugestoes.html', {'form': form, 'mensagem': mensagem})


def index(request):
    return render(request, 'publico_index.html')
