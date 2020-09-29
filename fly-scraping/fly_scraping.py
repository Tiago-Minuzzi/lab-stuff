#!/usr/bin/env python3
import os
import glob
import time
import pathlib
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Paths and type of files
home = Path.home()
csvs = glob.glob("test/*.txt")
drv = f"{home}/.local/bin/chromedriver" # path to browser driver
downf = f'{home}/Downloads/FlyBase_Fields_download.txt'
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
    # FIRST PAGE
    # Fill box with ids from file
    cf_afp = os.path.abspath(cf)
    brw_box = driver.find_element_by_id("idfile")
    brw_box.send_keys(cf_afp)
    # Select type of output (either file or browser)
    select = Select(driver.find_element_by_id("output"))
    select.select_by_value("File")
    # Click sumbmit button
    submeter = driver.find_element_by_id("submit") 
    submeter.click()
    # SECOND PAGE
    time.sleep(0.3)
    for FTR in FEATURES:
        FT = driver.find_element_by_id(FTR) 
        FT.click()
    # Get table
    get_table = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/input[1]")
    get_table.click()
    time.sleep(2)
    # Create new name
    _, cf_name = cf.split('/')
    cf_stem, _, _ = cf_name.split('.')
    new_name = f'{cf_stem}_flybase.csv'
    # Rename file
    os.rename(downf, new_name)
# Quit browser (to close tab only, use driver.close())
time.sleep(1)
driver.quit()