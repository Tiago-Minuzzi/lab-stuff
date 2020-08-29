#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Target site
fly_batch = "https://flybase.org/batchdownload"
# Browser driver
drv = "/home/tiago/.local/bin/chromedriver"
# Page
results_to = "/html/body/div[2]/div/div/form/fieldset/div[2]/div[1]/div[2]/div[3]/div/select/option[2]"

driver = webdriver.Chrome(drv)
driver.get(fly_batch)
search_box = driver.find_element_by_xpath('//*[@id="ids"]')
search_box.send_keys("FBgn0191532")
#search_box.submit()
driver.quit()
