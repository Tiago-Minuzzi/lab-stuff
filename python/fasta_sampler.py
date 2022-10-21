import sys
import random
from Bio.SeqIO.FastaIO import SimpleFastaParser

input_fasta = sys.argv[1]
n_sequences = int(sys.argv[2])

fasta_ids = ( fid[1:].strip() for fid in open(input_fasta).readlines() if fid.startswith('>') )
fids_sample = random.sample(list(fasta_ids), n_sequences)
with open(input_fasta) as fa:
    for fid, fsq in SimpleFastaParser(fa):
        if fid in fids_sample:
            record = f'>{fid}\n{fsq}'
            print(record)
    

