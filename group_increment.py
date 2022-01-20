# coding: utf-8
import sys
import pandas as pd

"""
- Example input:
 col1         col2
0     1       asdfas
1     1       sdfasd
2     1        foasf
3     2         sjfo
4     2        sjdof
5     3       hsdghs
6     4      fjkasdf
7     4  asdfasdfasf
8     4         sdfa
9     5         sadf

- Example output:
col1         col2
0  1.1       asdfas
1  1.2       sdfasd
2  1.3        foasf
3  2.1         sjfo
4  2.2        sjdof
5  3.1       hsdghs
6  4.1      fjkasdf
7  4.2  asdfasdfasf
8  4.3         sdfa
9  5.1         sadf
"""
arquivo = sys.argv[1]
coluna = 'col1'

def novo_nome(grupo,col_name):
    grupo[col_name] = [f"{str(v)}.{str(n+1)}" for n, v in enumerate(grupo[col_name].values)]
    return grupo

if __name__=="__main__":
    df = pd.read_csv(arquivo)
    grupos = df.groupby(coluna)
    new_df = grupos.apply(lambda g: novo_nome(g,coluna))
    print(new_df)
