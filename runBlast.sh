#!/usr/bin/env bash
# USAGE
# on command line run:
# bash runBlast.sh query.fasta subject.fasta blast_output.tsv
# Set blast output format
OUTFMT="6 qseqid sseqid qlen slen length qcovhsp evalue bitscore qseq sseq"
# Set max_target_seqs (MTGSEQS) and max_hsps (MHSPS)
MTGSEQS=5
MHSPS=5
# User input
QUERY=$1
SUBJC=$2
OUT=$3
# Run blast
if [[ -n $QUERY ]] && [[ -n $SUBJC ]] && [[ -n $OUT ]]; then # '-n' checks if var is not null.
blastn -query $QUERY -subject $SUBJC -max_target_seqs $MTGSEQS -max_hsps $MHSPS -outfmt "$OUTFMT" -out $OUT
else
    echo "Missing file(s)."
fi
