#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd


def repmask_format_out(input_file):
    with open(input_file) as arq:
        file_header = ['SW score',
                       'perc div.',
                       'perc del.',
                       'perc ins.',
                       'query sequence',
                       'query start',
                       'query end',
                       'query (left)',
                       'strand',
                       'matching repeat',
                       'repeat class/family',
                       'repeat start',
                       'repeat end',
                       'repeat (left)',
                       'ID']
        arq = arq.readlines()[3:]
        arq = [ item.strip().replace('*','') for item in arq ]
        arq = [ item.split() for item in arq ]
        df = pd.DataFrame(arq, columns = file_header)
    return  df

def main():
    entrada = sys.argv[1]
    df = repmask_format_out(entrada)
    df_count = df['repeat class/family'].value_counts().rename_axis('classification').reset_index(name='count')
    df.to_csv(f'{entrada}.csv',index=False)
    df_count.to_csv(f'{entrada}.count.csv',index=False)
    

if __name__ == "__main__":
    main()

