# Generated by Django 5.0.3 on 2024-04-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0002_alter_sugestao_situacao_alter_sugestao_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugestao',
            name='situacao',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('avaliada', 'Avaliada')], default='pendente', max_length=20),
        ),
    ]
