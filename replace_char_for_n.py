#!/usr/bin/env python3
import sys
fastin = sys.argv[1]
fastout = sys.argv[2]



def replace_for_n(in_fasta, out_fasta):
    seqs_by_ids = {}
    nts = "RYKMSWBDHV"
    with open(in_fasta, "r") as fas_in, open(out_fasta, "w") as fas_out:
        fas_in = fas_in.readlines()
        # Create dictionary
        for line in fas_in:
            line = line.strip()
            if line.startswith('>'):
                fas_id = line
                seqs_by_ids[fas_id] = ''
            else:
                for nt in nts:
                    line = line.upper().replace(nt,"N")
                seqs_by_ids[fas_id] += line
        # Write to file
        for fkey, fval in seqs_by_ids.items():
            fas_out.write(f'{fkey}\n{fval}\n')


replace_for_n(fastin, fastout)