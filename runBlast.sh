#!/usr/bin/env bash
# User input
QUERY=$1
SUBJC=$2
OUT=$3
# Set max_target_seqs (MTGSEQS) and max_hsps (MHSPS)
MTGSEQS=5
MHSPS=5
# Set blast output format
OUTFMT="6 qseqid sseqid qlen slen length qcovhsp evalue bitscore qseq sseq"
# Run blast
if [[ -n $QUERY ]] && [[ -n $SUBJC ]] && [[ -n $OUT ]]; then # '-n' checks if var is not null.
blastn -query $QUERY -subject $SUBJC -max_target_seqs $MTGSEQS -max_hsps $MHSPS -outfmt "$OUTFMT" -out $OUT
else
    echo "Missing file(s)."
fi
