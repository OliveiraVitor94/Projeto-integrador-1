from django.db import models


class Sugestao(models.Model):
    SITUACAO_CHOICES = (
        ('verificada', 'Verificada'),
        ('pendente', 'Pendente'),
    )

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)  # Adicionando campo telefone
    sugestao = models.TextField(max_length=200)
    data_sugestao = models.DateTimeField(auto_now_add=True)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='pendente')  # Adicionando campo situação

    def __str__(self):
        return self.nome 