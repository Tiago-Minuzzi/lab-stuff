#!/usr/bin/env python3
# Usage:
# python3 fasta_linearizer.py input.fasta output.fasta
import sys
fas_in = sys.argv[1]
fas_new = sys.argv[2]
# Open input and output files
with open(fas_in, 'r') as infasta, open(fas_new, 'w') as new_fasta:
# Linearize sequences
    f_seq = f_id = 0
    for line in infasta:
        line = line.strip()
        if line.startswith(">"):
            if f_seq > 0:
                new_fasta.writelines('\n')
            new_fasta.writelines(f'{line}\n')
            f_id += 1
        else:
            new_fasta.writelines(f'{line}')
        f_seq += 1
# print number of sequences
print(f"nº of sequences: {f_id}")