#!/usr/bin/env python3

import sys
from Bio import SeqIO

SCRIPT = sys.argv[0]

def count_nt(arquivo):
    with open(arquivo) as fasta:
        tamanhos = []
        for record in SeqIO.parse(fasta, 'fasta'):
            tamanhos.append(len(record.seq))
        contagem = sum(tamanhos)
        return contagem


if __name__ == '__main__':
    try:
        FASTA = sys.argv[1]
        contagem = count_nt(FASTA)
        mega_bases = round(contagem/1000000)
        print(f'There is {contagem} bases in {FASTA}.')
        print(f'Which is ~{mega_bases} Mb.')
    except IndexError:
        print('# No file entered.\n# Please enter file name/location.')
        print('# Run:')
        print(f'python3 {SCRIPT} your_file.fasta')
    except FileNotFoundError:
        print(f"File '{FASTA}' not found.")
