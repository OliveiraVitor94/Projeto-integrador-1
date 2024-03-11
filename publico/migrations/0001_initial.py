# Generated by Django 5.0.3 on 2024-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('sugestao', models.TextField()),
                ('data_sugestao', models.DateTimeField(auto_now_add=True)),
                ('situacao', models.CharField(choices=[('verificada', 'Verificada'), ('pendente', 'Pendente')], default='pendente', max_length=20)),
            ],
        ),
    ]
