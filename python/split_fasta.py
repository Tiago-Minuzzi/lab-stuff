#!/usr/bin/env python3
# coding: utf-8
import sys
from Bio import SeqIO
# User input
FASTA=sys.argv[1]
N_FILES=int(sys.argv[2])
# format file names
n_zeros=len(str(N_FILES))
# Read input file
with open(FASTA) as fasta:
    # store list of splitted file names
    arqs=[open(f'splitted_{str(i+1).zfill(n_zeros)}.fasta','w') for i in range(N_FILES)]
    # parse input fasta
    for num, line in enumerate(SeqIO.parse(fasta,"fasta")):
        fid=line.description
        seq=line.seq
        record=f'>{fid}\n{seq}\n'
        arqs[num % N_FILES].write(record)
    # close splitted files
    for f in arqs:
        f.close()
