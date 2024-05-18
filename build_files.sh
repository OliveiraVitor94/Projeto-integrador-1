#!/bin/bash

# Verificar se pip está disponível
if ! command -v /usr/local/bin/pip &> /dev/null
then
    echo "pip não encontrado, instalando..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    /usr/local/bin/python get-pip.py --user
    export PATH=$HOME/.local/bin:$PATH
fi

# Verificar se python está disponível
if ! command -v /usr/local/bin/python &> /dev/null
then
    echo "Python não encontrado, falhando..."
    exit 1
fi

# Instalar dependências do projeto
/usr/local/bin/pip install -r requirements.txt --user

# Executar quaisquer outros comandos necessários para construir o projeto
# Exemplo: coletar arquivos estáticos, realizar migrações, etc.
/usr/local/bin/python manage.py collectstatic --noinput
