#!/usr/bin/env bash

REFER="teste_ref.fasta"
READS="teste_montar.fasta"
PROJE="teste_kmers"

bowtie2-build  "$REFER" "$PROJE" &&
bowtie2 -x "$PROJE" -f -U "$READS" -S teste_kmers.sam &&
samtools view -b "$PROJE".sam -o teste_kmers.bam &&
samtools index "$PROJE".bam teste_kmers.bai &&
pilon --genome "$REFER" --bam "$PROJE".bam --output "$PROJE"_pilon
