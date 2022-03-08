#!/usr/bin/env python3
import os
import glob
# Get 'n' lines from files
NB_LINES = 2
# Files and foders
base_fasta = 'lin_unique_db_te_n_replace.fasta'
rep_fams = 'repbase_fams.txt'
folder = 'te_fams'
sufext = '_fam.fasta'
sample = 'master_sample_repbase.fasta'
# Read input files
with open(base_fasta) as dbte, open(rep_fams) as fams:
    dbte = dbte.readlines()
    fams = fams.readlines()
# Create folder
if not os.path.exists(folder):
    os.mkdir(folder)
# Create dictionary from base fasta
fas_dict = {}
for line in dbte:
    line = line.strip()
    if line.startswith('>'):
        fas_id = line
        fas_dict[fas_id] = ''
    else:
        fas_dict[fas_id] += line
# Create file arq_names
for name in fams:
    name = name.strip()
    arq_name = name.strip().replace("/","-")
    arq_name = arq_name.replace(" ","_")
    fasarq = f"{arq_name}{sufext}"
    fasarq = os.path.join(folder,fasarq)
    # Search patterns in dictionary
    with open(fasarq,"w") as arq:
        for k,v in fas_dict.items():
            kfam = k.split('\t')[1]
            if name == kfam and arq_name in fasarq:
                arq.write(f'{k}\n{v}\n')
# Read fasta files
for file in glob.glob(f'{folder}/*{sufext}'):
    with open(file,"r") as f, open(sample,"a") as fout:
        # Get 'n' samples from file
        for i in range(NB_LINES):
            fline = f.readline().strip()
            fout.write(fline+"\n")