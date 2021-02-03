#!/usr/bin/env python3
# Get uniq sequeces and write different ids in same id
# Usage: python3 fasta_rm_dup.py your_file.fasta
# Input file and script must be in the same folder
import sys
from Bio import SeqIO
# File, records list and sequence dictionary
in_fas = sys.argv[1]
glob_list=[]
fas_dict={}
# Read fasta and append records as pairs to list
for record in SeqIO.parse(in_fas, "fasta"):
    fid,fsq = record.id,str(record.seq)
    glob_list.append([fid,fsq])
# Turn sequences as keys and ids as values
for k,v in glob_list:
    if v not in fas_dict:
        fas_dict[v]=[] # store multiple values for each key
    fas_dict[v].append(k)
# Print fas_dict in fasta format
for ffseq,ffid in fas_dict.items():
    ffid='|'.join(ffid) # return ffid without brackets
    print(f'>{ffid}\n{ffseq}')
