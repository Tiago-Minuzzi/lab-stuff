library(ape)

entrada <- ''
saida <- ''

rename_labels <- function(tree, vec) {
    tree$tip.label <- vec
    return(tree)
}

tree <- read.tree(entrada)
names <- c('')
renamed_tree <- rename_labels(tree = tree, vec = names)
write.tree(renamed_tree,file = saida)
