from django.contrib import admin
from movimentacao import models
# Register your models here.
@admin.register(models.Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = 'nome_produto' , 'unidade' , 'saldo' , 'data_criacao' ,

@admin.register(models.Transacao)
class transacaoAdmin(admin.ModelAdmin):
    list_display = 'nome_produto' , 'quantidade' , 'tipo' , 'data' ,