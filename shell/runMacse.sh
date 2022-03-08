#!/usr/bin/env bash
MACSE=$HOME/sftw/macse_v2.05.jar
FASTAS=*.fasta

for FASTA in $FASTAS
do
    echo "Running macse for $FASTA..."
    java -jar $MACSE -prog alignSequences -seq $FASTA
    echo "Done!"
    echo "+++++"
done &&
echo "=================="
echo "All files aligned!"
echo "=================="
