#!/usr/bin/env python3
import os
import glob
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

# System paths
home = Path.home()
drv = f"{home}/.local/bin/chromedriver" # path to browser driver
# Target site
ncbi_nucl = "https://www.ncbi.nlm.nih.gov/nuccore"
# Ids file and fasta format
mitgen_ids = "sample.txt"
fasta_cds = "fasta_cds_aa"
# Open browser, read file
driver = webdriver.Chrome(drv)
# -----------------------------------
# Headless config
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=800x600')
# driver = webdriver.Chrome(executable_path=drv, chrome_options=options)
# -----------------------------------
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
		# Click 'send to'
		send_to = driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div[5]/div/div[1]/h4/a")
		send_to.click()
		time.sleep(1.5)
		# Choose coding sequence
		seq_form = driver.find_element_by_id("codeseq")
		seq_form.click()
		time.sleep(1.5)
		# Choose fasta format (aa or nt)
		cds_form = Select(driver.find_element_by_id("codeseq_format"))
		cds_form.select_by_value(fasta_cds)
		time.sleep(1.5)
		# Download files
		dwld_bt = driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div[5]/div/div[1]/div[2]/div[2]/button")
		dwld_bt.click()

time.sleep(2)
driver.quit()