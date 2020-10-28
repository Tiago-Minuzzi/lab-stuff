#!/usr/bin/env python3
# Save repbase repeat masking results
# Requirements: python3, requests and BeatifulSoup
# Install BeautifulSoup via pip
# Usage: python3 rep_scrap.py
import requests
from bs4 import BeautifulSoup as soup
# Prompt user for url and file name to save results
url = input("Paste repbase results url: ")
csv_out = input("Name for the output file: ")
# Header
HEADER = "Name,From,To,Name,From,To,Class,Dir,Sim,Pos/Mm:Ts,Score"
# Insert repbase results URL here
# url = 'https://www.girinst.org/cgi-bin/censor/show_results.cgi?id=10762&lib=root'
# Request page and fetch results
page = requests.get(url)
# Store the contents of the website
sp = soup(page.content, 'html.parser')
# Find tables
tables = sp.findAll('table')
size = len(tables[:-1]) # remove final statistics
# Get tables
rep_list = []
for table in range(size):
    for row in tables[table].find_all("tr")[1:]:
        row = row.get_text().replace(' ',',')
        rep_list.append(row)
# Get main results
res_size = int(len(rep_list)/2)
# Save results to file
with open(csv_out,"w") as rep_out:
    rep_out.write(HEADER+'\n')
    for item in rep_list[:res_size]:
        rep_out.write(item+"\n")