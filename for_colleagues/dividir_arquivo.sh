#!/usr/bin/env bash

# DIGITE O NOME DO ARQUIVO DENTRO DAS ASPAS
ARQUIVO="$1"

if [ -f $ARQUIVO ];then
    read -p "Dividir o arquivo em quantas partes? " NUMERO
    echo ""
    if ! [ $NUMERO -eq $NUMERO ] 2> /dev/null
    then
        echo "Por favor, digite um número." 
    else
            PREFIXO=$(basename $ARQUIVO)
            PREFIXO=${PREFIXO%.*}
            split -dn $NUMERO --numeric=1 --additional-suffix=".fasta" $ARQUIVO "$PREFIXO"_
            echo "O arquivo $ARQUIVO foi dividido em $NUMERO partes."
    fi
else
    echo "O arquivo $ARQUIVO não existe. Verifique o nome."
fi
