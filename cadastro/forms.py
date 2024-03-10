# No arquivo forms.py
from django import forms
from .models import Produtos

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'unidade', 'categoria']
