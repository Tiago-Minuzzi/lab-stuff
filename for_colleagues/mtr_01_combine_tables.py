#!/usr/bin/env python3
# coding: utf-8
'''
Para rodar o script é necessário Python3
e o pacote pandas.
- Para instalar o pandas use:
pip3 install --user pandas

Para rodar o script coloque o nomes dos arquivos
nas variáveis e depois rode o script no terminal.
- Uso:
python3 combine_tables.py
'''
import pandas as pd
# Arquivos
wolfpsort = 'wolf_loc_cell.tabular'
blastp = 'Blastp_db_12_genomas.tabular'
signalp = 'sinal_proteico.tabular'
promotores = 'promotor_prote.tabular'
hmmer = 'hmm_clean.csv'
saida = 'marcos_concat_tabs_exemplo.tsv'
# Ler arquivos
wps = pd.read_csv(wolfpsort, sep='\t')
blast = pd.read_csv(blastp, sep='\t')
sigp = pd.read_csv(signalp, sep='\t')
prom = pd.read_csv(promotores,sep='\t')
hmm = pd.read_csv(hmmer, sep='\t')
# Filtrar tabela do wolfpsort pelo rank
wps = wps.loc[wps['Rank']==1]
# Filtrar tabela do blast pelo bitscore
blast = blast.loc[blast.groupby('ID', sort=False)['bitscore'].idxmax()]
# Filtrar tabela dos promotores por score
prom = prom.loc[prom.groupby('ID', sort=False)['Score'].idxmax()]
# Mergir dataframes
wbp = pd.merge(wps,blast, on='ID', how='outer')
wbps = pd.merge(wbp,sigp, on='ID', how='outer')
wbpsp = pd.merge(wbps,prom, on='ID', how='outer')
wbpsph = pd.merge(wbpsp,hmm, on='ID', how='outer')
# Escrever dataframe final para arquivo tsv
wbpsph.to_csv(saida, sep='\t',index=False)