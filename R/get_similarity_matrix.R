library(ddCt)
library(bio3d)

# Files etc
inFasta = 'gpb_hosts_concatall.fasta'
outCSV = 'r_gpB_hosts_concatall.csv'
tabHTML = 'r_gpB_hosts_concatall_simat'
htmlTitle = 'Group B hosts similarity matrix'

# bio3d package
fastaArq = read.fasta(inFasta)
tabela = seqidentity(fastaArq, normalize=TRUE, similarity=T, ncore=1, nseg.scale=1)
tabela = round(tabela*100,2)

# write files
write.csv(tabela, file = outCSV)
tabela_csv = read.csv(outCSV)
write.htmltable(tabela_csv, file = tabHTML, title = htmlTitle)

# seqinr package
#aliFile = read.alignment('form_concatall_uniq_gpA_genes.fasta', format = 'fasta')
#matriz = as.matrix(dist.alignment(aliFile, matrix = 'identity'))

#tabela[,-1] = round(tabela[,-1]*100,2)
