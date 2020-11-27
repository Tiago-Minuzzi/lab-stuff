#!/usr/bin/env python3
# coding: utf-8
'''
Script para formatar e filtrar a tabela do HMMER.
Necessário python3 e o pacote pandas para rodar
o script.
- Para instalar o pacote pandas use:
pip3 install pandas
- Uso:
python3 mtr_00_hmm_table_filtering.py
'''
import pandas as pd
# Arquivo do hmmer e arquivo de saida
hmmer = "HMM_dominios_prot.txt"
hmm_saida = 'hmm_clean.tsv'
# Ler csv setando delimitador para qualquer espaço em branco.
hmm = pd.read_csv(hmmer, delim_whitespace = True)
# Colocar colunas na ordem desejada. ID precisa ser a primeira.
colunas = ['ID',
           'target_name',
           'accession',
           'accession.1',
           'E-value',
           'score',
           'bias',
           'E-value.1',
           'score.1',
           'bias.1',
           'exp',
           'reg',
           'clu',
           'ov',
           'env',
           'dom',
           'rep',
           'inc',
           'description_of_target']
# Reordenar colunas
hmm = hmm[colunas]
# Retirar colunas selecionadas sem valores
hmm.drop(['accession','accession.1','description_of_target'], axis=1, inplace=True)
# Pegar maior valor de score para cada id
hmm = hmm.loc[hmm.groupby('ID', sort=False)['score'].idxmax()]
# Escrever dataframe no formato tsv (tab separated values)
hmm.to_csv(hmm_saida,sep='\t', index=False)