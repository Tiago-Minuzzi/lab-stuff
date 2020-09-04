#!/usr/bin/env bash

# Mariana cancian master's pipeline 

# Set default working directory
export WD="."

# Softwares settings
BLAST="/home/labdros/software/ncbi-blast-2.10.0+/bin/blastn"
FQTOFA="$(which fastq_to_fasta)"

# Directories
FASTQIN="$WD/01_FASTQ"
MOSFQ="$WD/02_MOSFQ"
MOSFA="$WD/03_MOSFA"
CLEANFISH="$WD/04_CLEANFISH"
CLEANADAPT="$WD/05_CLEANADAPT"
SELFBLAST="$WD/06_SELFBLAST"
ONEHIT="$WD/07.01_ONEHIT"
MULTIHIT="$WD/07.02_MULTIHIT"
FILTHIT="$WD/08_FILTHIT"
SCOV="$WD/09_SCOV"
QSCOV70="$WD/10_QSCOV70"
IDSEQ="$WD/11_IDSEQ"
SAMPLEBLAST="$WD/12_SAMPLEBLAST"

# Files
REF1="$WD/00_reference/Mos_3.fasta"
REF2="$WD/00_reference/Mos_5.fasta"
GPAT1="$WD/00_reference/gpat1.tmp"
GPAT2="$WD/00_reference/gpat2.tmp"
ADAPTTOTAL="$WD/00_reference/adapt_total_limpo.txt"

# # M01: separar sequências que possuem mariner
mkdir -p $MOSFQ
for FASTQ in $FASTQIN/*.fastq;
do
	# Grep mos3 and mos5 patterns
	grep -v '>' $REF1 > $GPAT1
	grep -v '>' $REF2 > $GPAT2
	# Grep sequences with mos3 pattern
	grep -f $GPAT1 $FASTQ -B1 -A2 | sed '/^--$/d' > ${FASTQ%.fastq}_mos3.fastq &&
	mv $FASTQIN/*_mos3.fastq $MOSFQ && rm $GPAT1
	# Grep sequences with mos5 pattern
	grep -f $GPAT2 $FASTQ -B1 -A2 | sed '/^--$/d' > ${FASTQ%.fastq}_mos5.fastq &&
	mv $FASTQIN/*_mos5.fastq $MOSFQ && rm $GPAT2
done
# #_______________________________________________________________________________________________________________________________

# # M02: fastq to fasta
mkdir -p $MOSFA
for FMOSFQ in $MOSFQ/*.fastq;
do 
	$FQTOFA -i $FMOSFQ -o ${FMOSFQ%.fastq}."fa" &&
	mv $MOSFQ/*.fa $MOSFA
done
#_______________________________________________________________________________________________________________________________

# #M03: remove mariner and adapters (and "fish" sequence)
mkdir -p $CLEANFISH
for FMOSFA in $MOSFA/*.fa
do
	# Remove mariner and "fish" from mos3
	sed -e "s/TTATTCTAAGTATTTGCCGTCGC.*//;s/AAGTAGGGAATGTCGGTTCG.*//" $FMOSFA > ${FMOSFA%.fa}_clnfs.fa &&
	mv $MOSFA/*clnfs.fa $CLEANFISH
done
#_______________________________________________________________________________________________________________________________

# # M04: Remove adapters and arctifacts from sequences (NEW)
mkdir -p $CLEANADAPT
for FCLNFS in $CLEANFISH/*.fa
do
	sed -f <(sort -r "$ADAPTTOTAL" | sed 's/.*/s|&||/') $FCLNFS > ${FCLNFS%_clnfs.fa}_"clean.fa" &&
	mv $CLEANFISH/*clean.fa $CLEANADAPT
done
#_______________________________________________________________________________________________________________________________

# M05: blast de uma amostra contra ela mesma
mkdir -p $SELFBLAST
for CLEANFA in $CLEANADAPT/*_clean.fa
do
	$BLAST -query $CLEANFA -subject $CLEANFA -outfmt "7 qseqid sseqid pident length qlen slen evalue bitscore qcovs qstart qend sstart send qseq sseq" -out ${CLEANFA%_clean.fa}_blastout.tsv &&
	mv $CLEANADAPT/*blastout.tsv $SELFBLAST
done
#_______________________________________________________________________________________________________________________________

#M06: separar arquivos onehit de arquivos multihit 
mkdir -p $ONEHIT $MULTIHIT
for FSBLAST in $SELFBLAST/*blastout.tsv;
do
	# Cria arquivo com sequências com só um hit (elas mesmas)
	grep "# 1 hits found" -A1 $FSBLAST | sed '/^--$/d;/^#/d' > ${FSBLAST%_blastout.tsv}_onehit.tsv &&
	sed -i '1i qseqid\tsseqid\tpident\tlen\tqlen\tslen\tevalue\tbitscore\tqcovs\tqstart\tqend\tsstart\tsend\tqseq\tsseq' ${FSBLAST%_blastout.tsv}_onehit.tsv &&
	mv $SELFBLAST/*onehit.tsv $ONEHIT
	# Cria arquivo com as sequências com mais de um hit
	sed '/# 1 hits found/,+1 d;/^# /d' $FSBLAST > ${FSBLAST%_blastout.tsv}_multihit.tsv &&
	sed -i '1i qseqid\tsseqid\tpident\tlen\tqlen\tslen\tevalue\tbitscore\tqcovs\tqstart\tqend\tsstart\tsend\tqseq\tsseq' ${FSBLAST%_blastout.tsv}_multihit.tsv &&
	mv $SELFBLAST/*multihit.tsv $MULTIHIT	
done
#_______________________________________________________________________________________________________________________________

#M07: remover os hits contra ele mesmo e as repetições AxB ou BxA
mkdir -p $FILTHIT
for MHIT in $MULTIHIT/*multihit.tsv;
do
	python3 M07_filter_reciprocal_hits.py $MHIT ${MHIT%_multihit.tsv}_mhit_filt.tsv &&
	mv $MULTIHIT/*filt.tsv $FILTHIT
done
#_______________________________________________________________________________________________________________________________

# #M08: criação da tabela scov
mkdir -p $SCOV
for FSCOV in $FILTHIT/*filt.tsv;
do
	sed '1d' $FSCOV | 
	awk '{$16=int(($4/$6)*100)}1' |
	sed '1i qseqid\tsseqid\tpident\tlen\tqlen\tslen\tevalue\tbitscore\tqcovs\tqstart\tqend\tsstart\tsend\tqseq\tsseq\tscov' |
	awk '{ print $1,$2,$3,$4,$5,$6,$7,$8,$9,$16,$10,$11,$12,$13,$14,$15 }' |
	sed 's/ /\t/g' > ${FSCOV%_mhit_filt.tsv}_scov.tsv &&
	mv $FILTHIT/*scov.tsv $SCOV
done
#_______________________________________________________________________________________________________________________________

# #M08: sequências que deram blast devido ao adapt
# # Selecionar linhas com o adaptador
# grep CACTCTT $1 > $2
# # Selecionar linhas sem o adaptador
# grep -v CACTCTT $1 > $3
# #pegar ids da tabela que tem os adaptadores
# cut -f1 $2 > ids1.txt 
# cut -f2 $2 > ids2.txt 
# cat ids1.txt ids2.txt | sort | uniq > ids_adapter.txt && rm ids1.txt ids2.txt
# # Pegar sequencias com adaptador
# grep -A1 -f ids_adapter.txt $4 | sed '/^--$/d' > $5 && rm ids_adapter.txt
# #_______________________________________________________________________________________________________________________________

#M09: separar sequências iguais e pegar uma representante (q/scov>=70)
mkdir -p $QSCOV70
for QSCOV in $SCOV/*scov.tsv
do
	python3 M10_qcov70_filtro.py $QSCOV ${QSCOV%_scov.tsv}_qscov70.tsv &&
	mv $SCOV/*qscov70.tsv $QSCOV70
done
#_______________________________________________________________________________________________________________________________

# #M10: pegar as sequências correspondentes aos ids
# mkdir -p $IDSEQ
# for FIDSEQ in $QSCOV70/*qscov70.tsv
# do
# 	cut -f1 $FIDSEQ | sed "/qseqid/d" | sort | uniq > ids.txt
# 	grep -A1 -f ids.txt $FCLNFS | sed '/^--$/d' > ${FIDSEQ%_qscov70.tsv}_fastafinal.fa && 
# 	rm ids.txt 
# 	mv $QSCOV70/*fastafinal.fa $IDSEQ
# done
#---------------------------------------------------------------------------------------------------------------------------------

# ##comparação de amostras
# #M11: blast de uma amostra contra outra
# mkdir -P $SAMPLEBLAST 
# for FSPBLAST in $IDSEQ/*fastafinal.fa
# do
# 	$BLAST -query $1 -subject $2 -outfmt "7 qseqid sseqid pident length qlen slen evalue bitscore qcovs qstart qend sstart send qseq sseq" -out $3
# 	mv $IDSEQ/* $SAMPLEBLAST

# #_______________________________________________________________________________________________________________________________

# #M12: remove blast com adapt (ver se precisa)
# ##1 arquivo da tabela completa
# #$2 arquivo de saída com adapter
# #$3 arquivo de saída sem adapter
# #$4 ids com adapt coluna F1
# #$5 ids com adapt coluna F2

# # Selecionar linhas com o adaptador
# grep CACTCTT $1 > $2
# # Selecionar linhas sem o adaptador
# grep -v CACTCTT $1 > $3
# #pegar ids da tabela que tem os adaptadores
# cut -f1 $2 > ids1.txt 
# cut -f2 $2 > ids2.txt 
# cat ids1.txt | sort | uniq > $4 && rm ids1.txt 
# cat ids2.txt | sort | uniq > $5 && rm ids2.txt

# #_______________________________________________________________________________________________________________________________

# #M13: blast recíproco
# mkdir -p $RBHBLAST
# for FRBHBLAST in $SAMPLEBLAST
# do
# 	python2 M14_rbh.py $1 $2 1 2 10 high $3 &&
# 	mv $SAMPLEBLAST/* $RBHBLAST
# done
