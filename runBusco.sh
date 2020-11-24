ARQS=(*.fna)
for NAME in ${ARQS[@]}
do
    # Busco local or in conda
    #busco -l arthropoda_odb10 -i $NAME -o ${NAME%.fna} -m genome
    # Busco docker image
    docker run -u $(id -u) -v $(pwd):/busco_wd ezlabgva/busco:v5.beta.1_cv1 busco -i $NAME -o ${NAME%.fna} -m genome -l arthropoda_odb10
done
