#!/usr/bin/env python3
import os
import glob
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

# System paths
home = Path.home()
drv = f"{home}/.local/bin/chromedriver" # path to browser driver
# Target site
ena = "https://www.ebi.ac.uk/ena/browser/view/"
# Ids file and fasta format
mitgen_ids = "baixar.txt"
# Open browser, read file
driver = webdriver.Chrome(drv)
# Open browser, read files and send to form
with open(mitgen_ids,"r") as mti:
	ids_list = [line.strip() for line in mti]
	for ids_it in ids_list:
		link = ena+ids_it
		# Open link
		time.sleep(2)
		driver.get(link)
		driver.implicitly_wait(120)
		# Download files
		dwld_bt = driver.find_element_by_link_text("SET FASTA")
		dwld_bt.click()
driver.quit()
