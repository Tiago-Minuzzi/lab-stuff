#!/usr/bin/env python
# coding: utf-8
import pandas as pd

long = pd.read_csv('dsim_doublenz_long.csv',names=('id','sequence'))
short = pd.read_csv('dsim_doublenz_short.csv',names=('id','sequence'))

short['length']=short.sequence.str.len()
short = short[['id','length']]

long['length']=long.sequence.str.len()
long['not_detectable']=long['length'] - 600
long = long[['id','length','not_detectable']]

with pd.ExcelWriter('fragments_124.xlsx') as writer:
    short.to_excel(writer, sheet_name='short_frags')
    long.to_excel(writer, sheet_name='long_frags')
