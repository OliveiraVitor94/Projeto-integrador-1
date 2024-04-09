# Generated by Django 5.0.3 on 2024-04-08 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0005_rename_entradas_produtos_vendas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('unidade', models.CharField(choices=[('UN', 'Unidade'), ('PCT', 'Pacote'), ('L', 'Litros'), ('KG', 'Quilograma')], max_length=20)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('vendas', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('arrecadacao', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacao.produto'),
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
