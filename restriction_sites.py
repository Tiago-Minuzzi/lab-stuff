#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Tiago Minuzzi
"""
import sys
from Bio import SeqIO
from Bio.Restriction import *

INFILE=sys.argv[1]

with open(INFILE) as fasta:
    for record in SeqIO.parse(fasta, 'fasta'):
        fid = record.id
        sequencia = record.seq
        tamanho = len(record.seq)
        # Find restriction sites        
        sitiosHIII = HindIII.search(sequencia)
        sitiosERI = EcoRI.search(sequencia)
        allsites= sitiosHIII+sitiosERI
        allsites=list(set(allsites))
        allsites.sort()
        allsites.insert(0,0)
        for i,j in zip(allsites,allsites[1:]+[None]):
            sitio=f'{i+1}:{j}'
            sitio=sitio.replace('None',str(len(sequencia)))
            corte=sequencia[i:j]
            tam=len(corte)
            print(f'>{fid}|pos={sitio}|length={tam}\n{corte}')
