#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

DOMAIN = "https://flybase.org"
URL = "https://flybase.org/batchdownload"

def get_soup(url):
    return bs(requests.get(url).text, "html.parser")

for link in get_soup(URL).find_all('a'):
    file_link = link.get("href")
    print(file_link)
