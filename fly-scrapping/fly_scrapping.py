#!/usr/bin/env python3
import os
import glob
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Paths and type of files
csvs = glob.glob("test/*.ids.txt")
drv = "/home/tiago/.local/bin/chromedriver" # path to browser driver
# Target site
fly_batch = "https://flybase.org/batchdownload"
FEATURES = ("SYMBOL",
            "FEATURE_TYPE",
            "UNIPROT_PROTEIN_FAMILY",
            "GO_MOLECULAR_FUNCTION",
            "GO_BIOLOGICAL_PROCESS",
            "GO_CELLULAR_COMPONENT",
            "DROSOPHILA_ORTHOLOGS")
# Open browser, read files and send to form
driver = webdriver.Chrome(drv)
for cf in csvs:
    driver.get(fly_batch)
    with open(cf,"r") as cf_ids:
        cf_ids = cf_ids.read()
    # FIRST PAGE
    # Fill box with ids from file
        ids_box = driver.find_element_by_xpath('//*[@id="ids"]')
        ids_box.send_keys(cf_ids)
        # Select type of output (either file or browser)
        select = Select(driver.find_element_by_id("output"))
        select.select_by_value("File")
        # Click sumbmit button
        submeter = driver.find_element_by_id("submit") 
        submeter.click()
        # SECOND PAGE
        for FTR in FEATURES:
            FT = driver.find_element_by_id(FTR) 
            FT.click()
        # Get table
        get_table = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/input[1]")
        get_table.click()
# Quit browser (to close tab only, use driver.close())
time.sleep(1)
driver.quit()
