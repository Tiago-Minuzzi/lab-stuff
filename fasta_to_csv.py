#!/usr/bin/env python3

import os
import sys

FASTA = sys.argv[1]

def fasta_to_csv(in_fasta):                                                                                                                       
    fasta_name = os.path.basename(in_fasta)
    diretorio = os.path.abspath(os.path.dirname(in_fasta))
    csv_name, _ = os.path.splitext(fasta_name)
    csv_name = f'{csv_name}.csv'
    csv_out = os.path.join(diretorio, csv_name)
    fas_dict = {}
    with open(in_fasta,"r") as fasta, open(csv_out, "w") as fout:
    # Input file
        fasta = fasta.readlines()
        for linha in fasta:
            linha = linha.strip()
            if linha.startswith('>'):
                fid = linha[1:]
                fas_dict[fid] = ''
            else:
                fas_dict[fid] += linha
    # Output file
        for sid, seq in fas_dict.items():
            seq = seq.upper()
            if ',' in sid:
                sid = sid.replace(',','')
            fout.write(f'{sid},{seq}\n')


if __name__ == '__main__':
    fasta_to_csv(FASTA)
    print('Done!')
