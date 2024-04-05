# Generated by Django 5.0.3 on 2024-04-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0003_produtos_arrecadacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='saidas',
            new_name='vendas',
        ),
        migrations.AlterField(
            model_name='produtos',
            name='arrecadacao',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
    ]
