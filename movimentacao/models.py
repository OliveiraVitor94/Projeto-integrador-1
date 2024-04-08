from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Produto(models.Model):
    UNIDADE_CHOICES = (
        ('UN', 'Unidade'),
        ('PCT', 'Pacote'),
        ('L', 'Litros'),
        ('KG', 'Quilograma'),
    )

    nome = models.CharField(max_length=100, unique=True)
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, blank=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vendas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    arrecadacao = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.arrecadacao = self.vendas * self.preco
        super().save(*args, **kwargs)

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.produto.nome}: {self.quantidade}"

    def clean(self):
        if self.quantidade > self.produto.saldo:
            raise ValidationError(f'Quantidade de venda inválida. Saldo insuficiente. Saldo atual do produto: {self.produto.saldo}')

    def save(self, *args, **kwargs):
        self.full_clean()  # Chama o método clean() antes de salvar
        super().save(*args, **kwargs)
        # Após salvar, atualiza o saldo do produto e o total de vendas
        self.produto.saldo -= self.quantidade
        self.produto.vendas += self.quantidade
        self.produto.save()