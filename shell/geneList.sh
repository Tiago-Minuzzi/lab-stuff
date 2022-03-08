#!/usr/bin/env bash

MONTAGENS=(wolb_ga_assemb_ids.txt wolb_gb_assemb_ids.txt wolb_gAB_assemb_ids.txt)
SEQDIRS=busco_wolbs/WOLB*/run_rickettsiales_odb10/busco_sequences/single_copy_busco_sequences/
TOPN=50

for MONTAGEN in ${MONTAGENS[@]}
do
    MOUTPUT=${MONTAGEN%_assemb_ids.txt}_top"$TOPN"_gene_list.txt
    echo "Running for $MONTAGEN..."
    find $SEQDIRS -type f -name "*.fna" | grep -f $MONTAGEN | cut -d'/' -f6 | sort | uniq -c | sed 's/^[ \t]*//g;s/ /\t/' | sort -k1 -n | tail -n $TOPN > "$MOUTPUT" && echo "Done for $MONTAGEN." && echo ""
done
