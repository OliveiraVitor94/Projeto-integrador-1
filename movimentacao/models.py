from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cadastro.models import Colaboradores

class Produtos(models.Model):
    UNIDADE_CHOICES = (
        ('UN', 'Unidade'),
        ('PCT', 'Pacote'),
        ('L', 'Litros'),
        ('KG', 'Quilograma'),
    )

    nome_produto = models.CharField(max_length=100, unique=True)
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, blank=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    entradas = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    saidas = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    arrecadacao = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    def __str__(self):
        return self.nome_produto

class Transacao(models.Model):
    tipo = models.CharField(max_length=1, choices=(('E', 'ENTRADA'), ('S', 'SAÍDA')))
    nome_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.CASCADE, default="")  # Substitua 1 pelo ID do colaborador padrão

    def __str__(self):
        return f"Transação de {self.nome_produto.nome_produto}: {self.quantidade} ({self.tipo})"

@receiver(post_save, sender=Transacao)
def atualizar_saldo(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == 'E':
            instance.nome_produto.saldo += instance.quantidade
            instance.nome_produto.entradas += instance.quantidade
        elif instance.tipo == 'S':
            if instance.quantidade > instance.nome_produto.saldo:
                # Se a quantidade de saída for maior que o saldo, retorne uma exceção
                raise ValueError('Quantidade de saídas inválida. Saldo insuficiente.')
            instance.nome_produto.saldo -= instance.quantidade
            instance.nome_produto.saidas += instance.quantidade
        
        instance.nome_produto.save()

        # Calcular arrecadação
        instance.nome_produto.arrecadacao = instance.nome_produto.saidas * instance.nome_produto.preco
        instance.nome_produto.save()