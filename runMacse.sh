#!/usr/bin/env bash
MACSE=$HOME/sftw/macse_v1.01b.jar
FASTAS=all_*.fna

for FASTA in $FASTAS
do
    java -jar $MACSE -prog alignSequences -seq $FASTA
done
