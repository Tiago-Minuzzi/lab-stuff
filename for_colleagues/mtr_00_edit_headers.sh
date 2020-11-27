#!/usr/bin/env bash
# Arquivos
HMMER="HMM_dominios_prot.txt"
BLAST="Blastp_db_12_genomas.tabular"
PROMO="promotor_prote.tabular"
SIGNP="sinal_proteico.tabular"
WPSRT="wolf_loc_cell.tabular"
# Editar headers
sed -i 's/# target name/target_name/;s/ of /_of_/;s/query name/ID/;/#/d' $HMMER
sed -i "1 i ID\tsseqid\tpident\tlength\tmismatch\tgapopen\tqstart\tqend\tsstart\tsend\tevalue\tbitscore" $BLAST
sed -i "s/#Identifier/ID/" $PROMO
sed -i "s/^#//" $SIGNP
sed -i "s/^#//" $WPSRT
