from django.contrib import admin
from cadastro import models

# Register your models here.
@admin.register(models.Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = 'nome' , 'matricula' ,


@admin.register(models.Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = 'produto' , 'unidade' , 'saldo' ,

@admin.register(models.ProdutosVendas)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = 'produto' , 'unidade' , 'saldo' , 'preco' ,

