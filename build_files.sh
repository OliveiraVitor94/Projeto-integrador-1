#!/bin/bash

# Verificar se python está disponível
if ! command -v python &> /dev/null
then
    echo "Python não encontrado, verificando por python3..."
    if ! command -v python3 &> /dev/null
    then
        echo "Python não encontrado, falhando..."
        exit 1
    else
        PYTHON_CMD=python3
    fi
else
    PYTHON_CMD=python
fi

# Instalar o pip se necessário
if ! command -v pip &> /dev/null
then
    echo "pip não encontrado, instalando..."
    $PYTHON_CMD -m ensurepip --user
    export PATH=$HOME/.local/bin:$PATH
fi

# Instalar dependências do projeto
pip install -r requirements.txt --user

# Executar quaisquer outros comandos necessários para construir o projeto
# Exemplo: coletar arquivos estáticos, realizar migrações, etc.
$PYTHON_CMD manage.py collectstatic --noinput
