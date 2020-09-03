#!/usr/bin/env bash

# Mariana cancian master's pipeline 

# Set default working directory
export WD="."

# Softwares settings
BLAST="/home/tiago/Database/softwares/ncbi-blast-2.10.0+/bin/blastn"
FQTOFA="$(which fastq_to_fasta)"

# Directories
FASTQIN="$WD/01_FASTQ"
MOSFQ="$WD/02_MOSFQ"
MOSFA="$WD/03_MOSFA"
CLEANMOS="$WD/04_CLEANMOS"
SELFBLAST="$WD/05_SELFBLAST"

# Files
REF1="$WD/00_reference/Mos_3.fasta"
REF2="$WD/00_reference/Mos_5.fasta"
GPAT1="$WD/00_reference/gpat1.tmp"
GPAT2="$WD/00_reference/gpat2.tmp"
ADAPTTOTAL="$WD/00_reference/adapt_total_limpo.txt"

# M01: separar sequências que possuem mariner
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
#_______________________________________________________________________________________________________________________________

# M02: fastq to fasta
mkdir -p $MOSFA
for FMOSFQ in $MOSFQ/*.fastq;
do 
	$FQTOFA -i $FMOSFQ -o ${FMOSFQ%.fastq}."fa" &&
	mv $MOSFQ/*.fa $MOSFA
done
#_______________________________________________________________________________________________________________________________


# M0 3(4): Remove adapters and arctifacts from sequences (NEW)
mkdir -p $CLEANMOS
for FMOSFA in $MOSFA/*.fa
do
	sed -f <(sort -r "$ADAPTTOTAL" | sed 's/.*/s|&||/') $FMOSFA > ${FMOSFA%.fa}_"clean.fa" &&
	mv $MOSFA/*clean.fa $CLEANMOS
done
#_______________________________________________________________________________________________________________________________

# M04: blast de uma amostra contra ela mesma
mkdir -p $SELFBLAST
for CLEANFA in $CLEANMOS/*_clean.fa
do
	$BLAST -query $CLEANFA -subject $CLEANFA -outfmt "7 qseqid sseqid pident length qlen slen evalue bitscore qcovs qstart qend sstart send qseq sseq" -out ${CLEANFA%.fa}_blastout.tsv &&
	mv $CLEANMOS/*blastout.tsv $SELFBLAST
done
#_______________________________________________________________________________________________________________________________

# #M05: separar arquivos onehit de arquivos multihit 
# BLASTOUT=$1
# ONEHIT=$2
# MULTIHIT=$3
# # Cria arquivo com sequências com só um hit (elas mesmas)
# grep "# 1 hits found" -A1 $BLASTOUT | sed '/^--$/d;/^#/d' > $ONEHIT
# # Cria arquivo com as sequências com mais de um hit
# sed '/# 1 hits found/,+1 d;/^# /d' $BLASTOUT > $MULTIHIT
# # Adiciona cabeçalho ao arquivo.
# sed -i '1i qseqid\tsseqid\tpident\tlen\tqlen\tslen\tevalue\tbitscore\tqcovs\tqstart\tqend\tsstart\tsend\tqseq\tsseq' $MULTIHIT
# #_______________________________________________________________________________________________________________________________

# #M06: remover os hits contra ele mesmo e as repetições AxB ou BxA
# import pandas as pd
# import numpy as np
# import sys
# # Lê o arquivo de entrada
# df = pd.read_csv(sys.argv[1], sep="\t")
# # Remove hit da sequência com ela mesma.
# df=df[df["qseqid"]!=df["sseqid"]]
# # Deixa apenas um dos hits recíprocos
# df[['qlen','slen']] = df[['qlen','slen']].astype(str) #Turn the values into strings so you can create sortable list over it.
# df['aux'] = df[['qseqid','sseqid','qlen','slen']].values.tolist() #create a list of the 4 columns
# df['aux'] = df['aux'].apply(sorted).astype(str) #sort the list and treat it as a full string.
# df = df.drop_duplicates(subset='aux').drop(columns='aux') #drop the rows where the list is duplicate, that is, there is the same combination of Qid, Sid, L1 and L2.
# # Escreve resultado para arquivo
# df.to_csv(sys.argv[2], sep="\t",index=False)
# #_______________________________________________________________________________________________________________________________

# #M07: criação da tabela scov
# sed '1d' $1 | 
# awk '{$16=int(($4/$6)*100)}1' |
# sed '1i qseqid\tsseqid\tpident\tlen\tqlen\tslen\tevalue\tbitscore\tqcovs\tqstart\tqend\tsstart\tsend\tqseq\tsseq\tscov' |
# awk '{ print $1,$2,$3,$4,$5,$6,$7,$8,$9,$16,$10,$11,$12,$13,$14,$15 }' |
# sed 's/ /\t/g' > $2
# #_______________________________________________________________________________________________________________________________

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

# #M09: separar sequências iguais e pegar uma representante (q/scov>=70)
# import pandas as pd
# import sys

# df = pd.read_csv(sys.argv[1], sep='\t')
# id1=set(df['sseqid'])
# dfr=df[(~df['qseqid'].isin(id1)) & ((df['scov'] >= 70) | (df['qcovs'] >= 70))]
# dfr.to_csv(sys.argv[2],sep='\t', index=False)
# #_______________________________________________________________________________________________________________________________

# #M10: pegar as sequências correspondentes aos ids
# ##$1 tabela filtrada
# ##$2 fasta que tem todas as sequências
# ##$3 fasta para o blast final
# ##sequencias do fasta devem estar linearizadas

# cut -f1 $1 | sed "/qseqid/d" | sort | uniq > ids.txt
# grep -A1 -f ids.txt $2 | sed '/^--$/d' > $3 && rm ids.txt

# echo "Total de sequencias: $(grep -c '>' $3)"
# #---------------------------------------------------------------------------------------------------------------------------------

# ##comparação de amostras
# #M11: blast de uma amostra contra outra
# ~/software/ncbi-blast-2.10.0+/bin/blastn -query $1 -subject $2 -outfmt "7 qseqid sseqid pident length qlen slen evalue bitscore qcovs qstart qend sstart send qseq sseq" -out $3
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
# #!/usr/bin/env python

# # Input: two tabular BLAST outputs (e.g., -outfmt 6). Specify columns containing query ID and subject ID, criterion column (e-value, bit score), and whether to seek highest or lowest values from that column.
# # reciprocal_blast_hits.py a_vs_b b_vs_a col_query col_match col_score sort_order out_file
 
# #purpose: extract reciprocal best BLAST matches for a pair of datasets
# #usage: ./reciprocal_blast_hits.py a_vs_b b_vs_a col_query col_match col_score sort_order out_file
 
# #example, requires both blast hits attained highest bit score (12th column in blast's '-outfmt 6'):
# # ./reciprocal_blast_hits.py a_vs_b.blastout b_vs_a.blastout 1 2 12 high a_b.hits.out
 
# #example, requires both blast hits attained lowest evalue (11th column in -outfmt 6):
# # ./reciprocal_blast_hits.py a_vs_b.blastout b_vs_a.blastout 1 2 11 low a_b.hits.out
 
# import sys
 
# def stop_err( msg ):
#   sys.stderr.write("%s\n" % msg)
#   sys.exit(1)
# def get_col_index(col_str):
#   if col_str[0]=="c":
#     col_str = col_str[1:]
#   return int(col_str)-1
 
# def main():
# #Parse Command Line
#   try:
#     a_vs_b, b_vs_a, c_query, c_match, c_score, sort_order, out_file = sys.argv[1:]
#   except:
#     stop_err("Expect 7 arguments: two input files, column settings, output file")
 
 
#   want_highest = want_lowest = False
#   if sort_order == "high":
#     want_highest = True
#   elif sort_order == "low":
#     want_lowest = True
#   else:
#     stop_err("Sort order argument should be high or low")
 
#   if out_file in [a_vs_b, b_vs_a]:
#     stop_err("Output file would overwrite an input file")
 
#   c_query = get_col_index(c_query)
#   c_match = get_col_index(c_match)
#   c_score = get_col_index(c_score)
#   if len(set([c_query, c_match, c_score])) < 3:
#     stop_err("Need three different column numbers!")
 
#   best_a_vs_b = dict()
#   for line in open(a_vs_b):
#     if line.startswith("#"): continue
#     parts = line.rstrip("\n").split("\t")
#     a = parts[c_query]
#     b = parts[c_match]
#     score = float(parts[c_score])
#     if (a not in best_a_vs_b) \
#     or (want_highest and score > best_a_vs_b[a][1]) \
#     or (want_lowest and score < best_a_vs_b[a][1]):
#       best_a_vs_b[a] = (b, score, parts[c_score])
#   b_short_list = set(b for (b,score, score_str) in best_a_vs_b.values())
 
#   best_b_vs_a = dict()
#   for line in open(b_vs_a):
#     if line.startswith("#"): continue
#     parts = line.rstrip("\n").split("\t")
#     b = parts[c_query]
#     a = parts[c_match]
#     if a not in best_a_vs_b:
#       continue
#         #stop_err("The A-vs-B file does not have A-ID %r found in B-vs-A file" % a)
#     if b not in b_short_list: continue
#     score = float(parts[c_score])
#     if (b not in best_b_vs_a) \
#     or (want_highest and score > best_b_vs_a[b][1]) \
#     or (want_lowest and score < best_b_vs_a[b][1]):
#       best_b_vs_a[b] = (a, score, parts[c_score])
# #TODO - Preserve order from A vs B?
#   a_short_list = sorted(set(a for (a,score,score_str) in best_b_vs_a.values()))
 
#   count = 0
#   outfile = open(out_file, 'w')
#   outfile.write("#A_id\tB_id\tA_vs_B\tB_vs_A\n")
#   for a in a_short_list:
#     b = best_a_vs_b[a][0]
#     if b in best_b_vs_a and a == best_b_vs_a[b][0]:
#       outfile.write("%s\t%s\t%s\t%s\n" % (a, b, best_a_vs_b[a][2], best_b_vs_a[b][2]))
#       count += 1
#   outfile.close()
# #print "Done, %i RBH found" % count
# if __name__ == '__main__':
#   main()
