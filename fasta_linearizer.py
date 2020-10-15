#!/usr/bin/env python3
# Usage:
# python3 fasta_linearizer.py input.fasta output.fasta
import sys

# Open input and output files
with open(sys.argv[1], 'r') as infasta, open(sys.argv[2], 'w') as new_fasta:
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