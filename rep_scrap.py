#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.girinst.org/cgi-bin/censor/show_results.cgi?id=28590&lib=root'
page = requests.get(url)
sp = soup(page.content, 'html.parser')
tables = sp.findAll("table")
#tables = list(tables)
size = int(len(tables[:-1])/2-1)

HEADER = "Name,From,To,Name,From,To,Class,Dir,Sim,Pos/Mm:Ts,Score"

print(HEADER)
for table in tables[:size]:
    table = table.get_text().replace(' ',',')
    results = table[57:]
    print(results)
