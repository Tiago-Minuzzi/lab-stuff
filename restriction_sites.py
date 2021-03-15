#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Tiago Minuzzi
"""
from Bio import SeqIO
from Bio.Restriction import *


with open('dsim-all-chromosome-r2.02.fasta') as fasta:
    for record in SeqIO.parse(fasta, 'fasta'):
        fid = record.id
        sequencia = record.seq
        tamanho = len(record.seq)
        # Find restriction sites        
        sitiosHIII = HindIII.search(sequencia)
        sitiosERI = EcoRI.search(sequencia)
        # Find fragments from restriction sites
        hind_seqs = HindIII.catalyze(sequencia)
        eco_seqs = EcoRI.catalyze(sequencia)
        # HindIII
        # Get fragment sequence            
        for fragmentoH in hind_seqs:    
            print(f'>{fid}|{HindIII}\n{fragmentoH}')
            # Cut HindIII fragments with EcoRI
            frag_seqsEH = EcoRI.catalyze(fragmentoH)
            for fseqEH in frag_seqsEH:
                    fseqEH = str(fseqEH)
                    print(f'>{fid}|{EcoRI}x{HindIII}\n{fseqEH}')
        # EcoRI
        # Get fragment sequence            
        for fragmentoE in eco_seqs:
            print(f'>{fid}|{EcoRI}\n{fragmentoE}')
            # Cut EcoRI fragments with HindIII
            frag_seqsHE = HindIII.catalyze(fragmentoE)
            for fseqHE in frag_seqsHE:
                fseqHE = str(fseqHE)
                print(f'>{fid}|{HindIII}x{EcoRI}\n{fseqHE}')