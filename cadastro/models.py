from django.db import models
from django.utils import timezone
# Create your models here.

class Colaboradores(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    serie = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Produtos(models.Model):
    produto = models.CharField(max_length=100)
    unidade = models.CharField(max_length=20)
    categoria = models.CharField(max_length=10)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.produto

class ProdutosVendas(models.Model):
    produto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10)
    unidade = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.produto
