#!/bin/bash

# Instalar as dependências
pip install -r requirements.txt

# Migrar o banco de dados
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput
