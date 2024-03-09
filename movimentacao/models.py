from cadastro.models import Produtos
from cadastro.models import Colaboradores

from django.db import models
from django.utils import timezone
# Create your models here.

class Entradas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name='entradas_produto')
    matricula = models.ForeignKey(Colaboradores, on_delete=models.CASCADE, related_name='matricula_colaborador')
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def serie(self):
        return self.matricula.serie

    def nome(self):
        return self.matricula.nome

    def categoria(self):
        return self.produto.categoria

    def unidade(self):
        return self.produto.unidade

    def __str__(self):
        return f"Entrada {self.id}"

