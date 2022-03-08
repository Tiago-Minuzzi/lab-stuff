#!/usr/bin/env python3

import os
import sys
import glob
import argparse
from Bio import SeqIO

# Initialize argument parser
parser = argparse.ArgumentParser(prog='get_len.py',
                                usage='python3 %(prog)s --input file/directory [options]',
                                description='Get sequence length for file(s).')
# Set argument flags
parser.add_argument('-i','--input',
                    help='Input file or directory',
                    type=str,
                    required=True)
parser.add_argument('-t','--type',
                    default='f',
                    choices=('f','d'),
                    help='Set type of input (file or directory)',
                    type=str)
parser.add_argument('-e','--extension',
                    default='fasta',
                    help='Set file extension. Default: fasta',
                    type=str)
# Store arguments
args = parser.parse_args()

# Read file and get sequence length
def fas_len(arq):
    with open(arq) as fasta:
        print('')
        print(f'# {os.path.basename(arq)} sequences:')
        for record in SeqIO.parse(fasta,'fasta'):
            print(f'    - {record.description} has length: {len(record.seq)}')


# Initialize program
if __name__ == '__main__':
    # if input is file
    if args.type == 'f':
        FAS=args.input
        fas_len(FAS)
    # if input is directory
    elif args.type == 'd':
        EXT=args.extension
        INP=args.input
        FASTAS=glob.glob(os.path.join(INP,f'*.{EXT}'))
        for FAS in FASTAS:
            fas_len(FAS)
