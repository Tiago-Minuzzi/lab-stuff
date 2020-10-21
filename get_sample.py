#!/usr/share/env python3

import sys
import random

with open(sys.argv[1]) as fasta:
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
samples = random.sample(list(fas_group),100)

for sample in samples:
    print(sample[0]+'\n'+sample[1])