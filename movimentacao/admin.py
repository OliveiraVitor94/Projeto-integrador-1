from django.contrib import admin
from .models import Produtos, Transacao

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'unidade', 'preco', 'entradas', 'saidas', 'saldo', 'data_criacao', 'arrecadacao')

admin.site.register(Produtos, ProdutosAdmin)

class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome_produto', 'quantidade', 'data')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValueError as e:
            self.message_user(request, f"Erro: {e}", level='ERROR')

admin.site.register(Transacao, TransacaoAdmin)
