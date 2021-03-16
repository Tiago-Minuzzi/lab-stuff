#!/usr/bin/python
import sys
from Bio import SeqIO
# Input file
FastaFile = sys.argv[1]
# Desired sequence length
valor = int(sys.argv[2])
# Read fasta and sequences
with open(FastaFile) as fasta:
    for rec in SeqIO.parse(fasta, 'fasta'):
        name = rec.id
        seq = rec.seq
        seqLen = len(rec)
        if seqLen >= valor:
            print(f'>{name}\n{seq}')
