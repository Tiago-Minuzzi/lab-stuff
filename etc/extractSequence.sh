#!/usr/bin/env bash
FASTA=WOLB0762_CACQTW01.fasta
NEWFASTA=${FASTA%.fasta}_pubmlst_genes.fasta
POSITIONS=$(cut -f4-6 WOLB0762_CACQTW01_pubmlst_results.tsv | sed "/position/d;/^$/d;s/\t/:/;s/\t/-/")
# Use samtools to extract positions from pubmlst coordinates
if [[ ! -f $NEWFASTA ]];then 
    for GENE in $POSITIONS
        do
            samtools faidx $FASTA $GENE >> $NEWFASTA 
        done
else
    echo "$NEWFASTA already exists."
fi
