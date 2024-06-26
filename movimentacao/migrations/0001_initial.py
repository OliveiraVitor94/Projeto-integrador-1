# Generated by Django 5.0.3 on 2024-05-13 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caixa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('unidade', models.CharField(choices=[('UN', 'Unidade'), ('PCT', 'Pacote'), ('L', 'Litros'), ('KG', 'Quilograma')], max_length=20)),
                ('quantidade_inicial', models.IntegerField(default=0)),
                ('saldo', models.IntegerField(default=0, editable=False)),
                ('vendas', models.IntegerField(default=0, editable=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('arrecadacao', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('saldo', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacao.caixa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacao.produto')),
            ],
        ),
    ]
