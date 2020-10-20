#!/usr/bin/env python3
# Remove duplicated sequences in fasta file
# Usage: python3 fasta_rm_dup.py your_file.fasta
# Input file and script must be in the same folder

import sys
from Bio import SeqIO

in_fas = sys.argv[1]
seen = []
records = []
dup_seen = []
dup_records = []
# examples are in sequences.fasta
for record in SeqIO.parse(in_fas, "fasta"):
    if str(record.seq) not in seen:
        seen.append(str(record.seq))
        records.append(record)
    else:
        dup_seen.append(str(record.seq))
        dup_records.append(record)
# printing to console
# for record in records:
#     print(f'>{record.name}')
#     print(record.seq)

# writing to a fasta file
SeqIO.write(records, f"unique_{in_fas}", "fasta")
SeqIO.write(dup_records, f"dup_{in_fas}", "fasta")
