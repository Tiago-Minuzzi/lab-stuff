#!/usr/bin/env python3

with open("blastout_dbte_only.csv","r") as bout:
    bout = bout.readlines()
    for line in bout:
        qseqid, sseqid, qlen, slen, length, qcovhsp, evalue, bitscore, qseq, sseq = line.split("\t")
        if qlen != slen:
            print(f"## {qseqid} é diferente de {sseqid}")
            print(f">> qlen: {qlen}, slen: {slen}")
            print("======================")