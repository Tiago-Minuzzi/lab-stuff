# coding: utf-8
from Bio import SeqIO
arquivo='dmel-all-chromosome-r6.41.fasta'
KMER=100
with open(arquivo) as fasta:
    for record in SeqIO.parse(fasta,'fasta'):
        # fasta id
        fid=record.id
        # fasta sequence
        sequence=str(record.seq)
        # Get number of kmers per sequence
        n_kmers=len(sequence) - KMER + 1
        # Create kmer generator
        kmer_gen=((sequence[i:i+KMER],i,i+KMER) for i in range(n_kmers))
        # Iterate over generators
        for (item,v1,v2) in kmer_gen:
            print(item,v1,v2)
