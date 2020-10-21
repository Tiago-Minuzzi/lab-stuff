#!/usr/bin/env python3
# Save repbase repeat masking results
# Replace the url with your results url
# Usage: python3 rep_scrap.py
import requests
from bs4 import BeautifulSoup as soup
# Insert repbase results URL here
url = 'https://www.girinst.org/cgi-bin/censor/show_results.cgi?id=28590&lib=root'
# Request page and fetch results
page = requests.get(url)
sp = soup(page.content, 'html.parser')
tables = sp.findAll("table")
# Calculate size to extract unique results
size = int(len(tables[:-1])/2-1)
# Header
HEADER = "Name,From,To,Name,From,To,Class,Dir,Sim,Pos/Mm:Ts,Score"
# Print results
print(HEADER)
for table in tables[:size]:
    table = table.get_text().replace(' ',',')
    results = table[57:]
    print(results)
