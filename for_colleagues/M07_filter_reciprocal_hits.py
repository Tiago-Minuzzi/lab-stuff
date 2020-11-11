#!/usr/bin/env python
# coding: utf-8
"""
==============================================

Para usar o script digite no terminal:

python3 mari_filter_reciprocal_hits.py arquivo_entrada_multihit.tsv arquivo_saida.tsv

==============================================
"""

import pandas as pd
import numpy as np
import sys
# Lê o arquivo de entrada
df = pd.read_csv(sys.argv[1], sep="\t")
# Remove hit da sequência com ela mesma.
df=df[df["qseqid"]!=df["sseqid"]]
# Deixa apenas um dos hits recíprocos
df[['qlen','slen']] = df[['qlen','slen']].astype(str) #Turn the values into strings so you can create sortable list over it.
df['aux'] = df[['qseqid','sseqid','qlen','slen']].values.tolist() #create a list of the 4 columns
df['aux'] = df['aux'].apply(sorted).astype(str) #sort the list and treat it as a full string.
df = df.drop_duplicates(subset='aux').drop(columns='aux') #drop the rows where the list is duplicate, that is, there is the same combination of Qid, Sid, L1 and L2.
# Escreve resultado para arquivo
df.to_csv(sys.argv[2], sep="\t",index=False)
