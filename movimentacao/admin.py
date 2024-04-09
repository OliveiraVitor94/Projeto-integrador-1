from django.contrib import admin
from .models import Produto, Venda

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id' , 'nome', 'unidade', 'quantidade_inicial' , 'preco', 'vendas', 'saldo', 'arrecadacao', 'data_criacao')

admin.site.register(Produto, ProdutoAdmin)

class VendaAdmin(admin.ModelAdmin):
    list_display = ('id','produto', 'quantidade', 'data')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            self.message_user(request, f"Erro: {e}", level='ERROR')

admin.site.register(Venda, VendaAdmin)
