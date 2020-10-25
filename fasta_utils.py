#!/usr/bin/env python3
import sys

def remove_ext(fasta_file):
    if '/' in fasta_file:
        *_, fasta_name = fasta_file.split('/')
        base, _ = fasta_name.split('.')
        return base
    else:
        base, _ = fasta_file.split('.')
        return base

def linear_fasta(in_fasta):
    out_fasta = remove_ext(in_fasta)
    fas_dict = {}
    with open(in_fasta,"r") as fasta, open(f"lin_{out_fasta}.fasta", "w") as fout:
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

def fasta_to_csv(in_fasta):
    out_fasta = remove_ext(in_fasta)
    fas_dict = {}
    with open(in_fasta,"r") as fasta, open(f"{out_fasta}.csv", "w") as fout:
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
            fout.write(f'{sid},{seq}\n')