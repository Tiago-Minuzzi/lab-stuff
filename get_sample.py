#!/usr/share/env python3
# Get sammple from fasta file

import sys
import random

in_fasta = sys.argv[1]
N_SEQS = int(sys.argv[2])

with open(in_fasta,'r') as fasta:
    fasta = fasta.readlines()

fids = []
seqs = []
for linha in fasta:
    linha = linha.strip()
    if linha.startswith('>'):
        fids.append(linha)
    else:
        seqs.append(linha)

fas_group = zip(fids,seqs)
samples = random.sample(list(fas_group), N_SEQS)

for sample in samples:
    print(sample[0]+'\n'+sample[1])