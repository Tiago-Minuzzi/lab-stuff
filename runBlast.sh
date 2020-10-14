#!/usr/bin/env bash
QUERY=$1
SUBJC=$2
OUTF=$3

blastn -query $QUERY -subject $SUBJC -max_target_seqs 5 -max_hsps 5 -outfmt "6 qseqid sseqid qlen slen length qcovhsp evalue bitscore qseq sseq" -out $OUTF
