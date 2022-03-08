#!/usr/bin/env bash

# Create directory for fasta files
FDIR="fastas"
mkdir -p $FDIR
# Loop through tsv files
for ARQ in *.tsv
do
    # filtered tsv file
    TSV=scov_"$ARQ"
    # fasta sequences from filtered tsv file
    FASTA=${TSV%.tsv}.fasta
    awk '{$11=int(($5/$4)*100)}1' $ARQ | awk '{ print $1,$2,$3,$4,$5,$6,$11,$7,$8,$9,$10 }' | sed 's/ /\t/g' | awk '$7 >= 90' > $TSV &&
    cut -f1,10 $TSV | sed 's/^/&>/;s/\t/\n/' > "$FDIR"/"$FASTA" 
done &&
echo "Done!"
