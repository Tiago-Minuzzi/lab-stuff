#!/usr/bin/env python3
import os
import glob
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# System paths
home = Path.home()
drv = f"{home}/.local/bin/chromedriver" # path to browser driver
# Target site
ncbi_nucl = "https://www.ncbi.nlm.nih.gov/genome"
# Ids file and fasta format
mitgen_ids = "wolbachia_hosts.txt"
# Open browser, read file
driver = webdriver.Chrome(drv)
# Open browser, read files and send to form

with open(mitgen_ids,"r") as mti:
	ids_list = [line.strip() for line in mti]
	for ids_it in ids_list:
		time.sleep(1)
		driver.get(ncbi_nucl)
		time.sleep(2)
		# SEARCH FORM
		# Search term in form box
		search_id = driver.find_element_by_id("term")
		search_id.send_keys(ids_it)
		time.sleep(0.5)
		# Click search button
		search_bt = driver.find_element_by_id("search")
		search_bt.click()
		time.sleep(2)
		# GET FASTA
		# Download files
		try:
			dwld_bt = driver.find_element_by_css_selector("span.shifted:nth-child(6) > a:nth-child(1)")
			dwld_bt.click()
		except NoSuchElementException:
			print(f"No genome available for {ids_it}.")
			pass

time.sleep(2)
driver.quit()
