#!/usr/bin/env python3
# Usage
# python3 fasta_linearizer.py input.fasta
import os
import sys

FASTA=sys.argv[1]

def linear_fasta(in_fasta):
    diretorio = os.path.abspath(os.path.dirname(in_fasta))
    fasta_name = os.path.basename(in_fasta)
    out_fasta = f'lin_{fasta_name}'
    out_fasta = os.path.join(diretorio, out_fasta)
    fas_dict = {}
    with open(in_fasta,"r") as fasta, open(out_fasta, "w") as fout:
    # Input file
        fasta = fasta.readlines()
        for linha in fasta:
            linha = linha.strip()
            if linha.startswith('>'):
                fid = linha
                fas_dict[fid] = ''
            else:
                fas_dict[fid] += linha
    # Output file
        for sid, seq in fas_dict.items():
            seq = seq.upper()
            fout.write(f'{sid}\n{seq}\n')

if __name__ == '__main__':
    linear_fasta(FASTA)
    print('Done!')
