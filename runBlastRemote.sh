#!/usr/bin/env bash
QUERY=$1
OUTF=$2
DBTYPE=nt

blastn -query $QUERY -db $DBTYPE -max_target_seqs 5 -max_hsps 5 -outfmt "7 qseqid qlen stitle sacc slen length qcovhsp evalue bitscore" -out $OUTF -remote
