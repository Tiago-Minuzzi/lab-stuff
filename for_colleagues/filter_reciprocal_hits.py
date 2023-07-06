# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np

df = pd.read_csv("159_nmar_multihits.tsv", sep="\t")
df

df=df[df["qid"]!=df["sid"]]

df

df[['qlen','slen']] = df[['qlen','slen']].astype(str) #Turn the values into strings so you can create sortable list over it.
df['aux'] = df[['qid','sid','qlen','slen']].values.tolist() #create a list of the 4 columns
df['aux'] = df['aux'].apply(sorted).astype(str) #sort the list and treat it as a full string.
df = df.drop_duplicates(subset='aux').drop(columns='aux') #drop the rows where the list is duplicate, that is, there is the same combination of Qid, Sid, L1 and L2.

df

df.to_csv("159_filt_nmar_multihits.tsv",sep="\t",index=False)


