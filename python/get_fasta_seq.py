#!/usr/bin/env python3
# Created by Tiago Minuzzi, 2020.

# Files
in_fasta = "teste.fasta"
in_ids = "ids.txt"
out_fasta = "res_fas.fa"
# Empty dictionary to store sequences
fas_dict = {}
# Read reference fasta file
with open(in_fasta, "r") as fasta:
	fasta=fasta.readlines()
	for linha in fasta:
		linha = linha.strip()
		if linha.startswith(">"):
			kl = linha[1:]
			fas_dict[kl] = ''
		else:
			fas_dict[kl] = linha.upper()
# Open ids file and create output file
with open(in_ids,"r") as ides, open(out_fasta,'w') as fas_out:
	ides = ides.read()
	for sid, sseq in fas_dict.items():
		# Search ids from dict in ids file
		if sid in ides:
			# Write wanted sequences to file
			fas_out.write(f'>{sid}'+'\n'+f'{sseq}'+'\n')
