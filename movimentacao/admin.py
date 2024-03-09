from django.contrib import admin
from movimentacao import models
# Register your models here.
@admin.register(models.Entradas)
class EntradasAdmin(admin.ModelAdmin):
    list_display = 'produto' , 'unidade' , 'quantidade' , 'categoria' , 'nome' , 'serie',