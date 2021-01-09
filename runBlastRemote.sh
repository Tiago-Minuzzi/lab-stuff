#!/usr/bin/env bash
# User options
DBTYP=nt # database (nt or nr)
MTGSQ=5 # max_target_seqs
MHSPS=5 # max_hsps
OUTFM="7 qseqid qlen stitle sacc slen length qcovhsp evalue bitscore"
# User input/output
QUERY=$1
OUTFL=$2
# Run blast
if [[ -n $QUERY ]] && [[ -n $OUTFL ]]; then # '-n' checks if var is not null.
    blastn -query $QUERY -db $DBTYP -max_target_seqs $MTGSQ -max_hsps $MHSPS -outfmt "$OUTFM" -out $OUTFL -remote
else
    echo "Missing file(s)."
fi
