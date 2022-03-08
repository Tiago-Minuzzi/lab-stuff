library(ape)

tree<-read.tree("file.tre")
DistMatrix<-cophenetic(tree)
write.csv(DistMatrix,'tree_dist_matrix.csv')
