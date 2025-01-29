#!/usr/bin/env python3
# Get uniq sequeces and write different ids in same id
# Usage: python3 fasta_rm_dup.py your_file.fasta
# Input file and script must be in the same folder
import sys
from collections import defaultdict
from Bio.SeqIO.FastaIO import SimpleFastaParser
# File, records list and sequence dictionary
in_fas = sys.argv[1]
glob_list=[]
fas_dict=defaultdict(list)
group_n = 0
# Read fasta and append records as pairs to list
with open(in_fas) as fa:
    for fid, fsq in SimpleFastaParser(fa):
        fas_dict[fsq].append(fid)

# Print fas_dict in fasta format
for ffseq, ffid in fas_dict.items():
    group_n+=1
    count = len(ffid)
    ffid='|'.join(ffid) # return ffid without brackets
    print(f'>seq_{group_n};count={count};{ffid}\n{ffseq}')
