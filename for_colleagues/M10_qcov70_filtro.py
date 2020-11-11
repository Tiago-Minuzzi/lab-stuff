import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep='\t')
id1=set(df['sseqid'])
dfr=df[(~df['qseqid'].isin(id1)) & ((df['scov'] >= 70) | (df['qcovs'] >= 70))]
dfr.to_csv(sys.argv[2],sep='\t', index=False)
