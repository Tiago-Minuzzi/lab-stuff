#/usr/bin/env bash
# run_arthropoda_odb10/busco_sequences/single_copy_busco_sequences

ARQUIVOS=orthoCodes.txt
DIRETORIOS=org_dirs.txt
for ARQUIVO in $(cat $ARQUIVOS)
do
    if [[ ! -f all_"$ARQUIVO" ]];then
        tail -n +1 $(find */run_arthropoda_odb10/busco_sequences/single_copy_busco_sequences/ -name $ARQUIVO) | sed 's/^==> />/;/unknown description/d;/^$/d;s|/run_arthropoda_odb10/busco_sequences/single_copy_busco_sequences/|_|;s/ <==$//;s/_/-/' | perl -pe 's/_GCF.+_genomic//;s/_GCA_.+_genomic//' >> all_"$ARQUIVO" && echo "All $ARQUIVO are now concatenated."
    else
        echo "All $ARQUIVO already concatenated."
    fi
done
