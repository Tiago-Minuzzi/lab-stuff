#!/usr/bin/env python3
# Remove duplicated sequences in fasta file
# This script removes duplicated sequences even though they have different id's.
# Usage: python3 fasta_rm_dup.py your_file.fasta

import sys
from Bio import SeqIO

in_fas = sys.argv[1]
seen = []
records = []
# Read fasta and append to lists
for record in SeqIO.parse(in_fas, "fasta"):
    if str(record.seq) not in seen:
        seen.append(str(record.seq))
        records.append(record)

# printing to console
# for record in records:
#     print(f'>{record.name}')
#     print(record.seq)

# Write to new fasta file
SeqIO.write(records, f"unique_{in_fas}", "fasta")
