#!/usr/bin/env python3
import os
import shutil
import subprocess as sp
# Files
FASTA='WOLB0200_CACPYF01.fasta'
COORD='wolb0200_pubmlst.tsv'
STSDIR='sts_res'
# Use samtools to extract positions from pubmlst coordinates
with open(COORD) as COORD:
    next(COORD)
    COORD=COORD.readlines()
    if not os.path.isdir(STSDIR):
        os.mkdir(STSDIR)
    for coord in COORD:
        locus,*_,contig,inicio,fim=coord.strip().split('\t')
        position=f'{contig}:{inicio}-{fim}'
        FASLOC = f'{locus}.fasta'
        with open(FASLOC, 'a') as fasloc:
            stres = sp.run(['samtools','faidx', FASTA, position], capture_output = True, text = True)
            fasloc.write(stres.stdout)
            shutil.move(FASLOC,f'{STSDIR}/{FASLOC}')
