from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cadastro.models import Colaboradores

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=100)
    unidade = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_produto

class Transacao(models.Model):
    nome_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=(('E', 'ENTRADA'), ('S', 'SAÍDA')))
    data = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.CASCADE, default="")  # Substitua 1 pelo ID do colaborador padrão
    def __str__(self):
        return f"Transação de {self.nome_produto.nome_produto}: {self.quantidade} ({self.tipo})"

@receiver(post_save, sender=Transacao)
def atualizar_saldo(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == 'E':
            instance.nome_produto.saldo += instance.quantidade
        elif instance.tipo == 'S':
            instance.nome_produto.saldo -= instance.quantidade
        instance.nome_produto.save()
