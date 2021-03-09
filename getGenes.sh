#!/usr/bin/env bash

geneConcat(){
    GENES=$(cut -f2 $1)
    MONTAGENS=$2
    DIRETORIO=$3

    mkdir -p $DIRETORIO
    echo "Running analysis for $DIRETORIO..."
    for GENE in $GENES
    do
        cat $(find busco_wolbs/WOLB*/run_rickettsiales_odb10/busco_sequences/single_copy_busco_sequences/ -type f -name "$GENE" | grep -f "$MONTAGENS") >> "$DIRETORIO"/gpAB_all_"${GENE/fna/fasta}" && echo "    -${GENE%.fna} files concatenation done."
    done && echo "$DIRETORIO done!" && echo ""
}

geneConcat "wolb_gAB_top50_gene_list.txt" "wolb_gAB_assemb_ids.txt" "gpAB"
geneConcat "wolb_ga_top50_gene_list.txt" "wolb_ga_assemb_ids.txt" "gpA"
geneConcat "wolb_gb_top50_gene_list.txt" "wolb_gb_assemb_ids.txt" "gpB"
