#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
fly_batch = "https://flybase.org/batchdownload"
chrdrv = "/home/tiago/.local/bin/chromedriver"
results_to = "/html/body/div[2]/div/div/form/fieldset/div[2]/div[1]/div[2]/div[3]/div/select/option[2]"
next_button = "//*[@id="submit"]"

driver = webdriver.Chrome(chrdrv)
driver.get(fly_batch)
search_box = driver.find_element_by_xpath('//*[@id="ids"]')
search_box.send_keys("FBgn0191532")
#search_box.submit()
driver.quit()


#gecko="/usr/bin/geckodriver"
#
#cap = DesiredCapabilities().FIREFOX
#cap["marionette"] = False
#
#firefox = webdriver.Firefox(capabilities=cap, executable_path=gecko)
##firefox.get("https://flybase.org/batchdownload")
#firefox.get("https://google.com.br")

#firefox.quit()
