from selenium import webdriver
from selenium.webdriver.support.ui import Select

arquivo_ids = "/home/tiago/Database/softwares/my_git/lab-stuff/fly-scrapping/ids.test.csv" 
with open(arquivo_ids,"r") as arq_ids:
    arq_ids = arq_ids.read()

# Browser driver
fly_batch = "https://flybase.org/batchdownload"
drv = "/home/tiago/.local/bin/chromedriver"
driver = webdriver.Chrome(drv)
driver.get(fly_batch)

# FIRST PAGE
# Fill box with ids from file
ids_box = driver.find_element_by_xpath('//*[@id="ids"]')
ids_box.send_keys(arq_ids)
# Select type of output (either file or browser)
select = Select(driver.find_element_by_id("output"))
select.select_by_value("File")
# Click sumbmit button
submeter = driver.find_element_by_id("submit") 
submeter.click()

#SECOND PAGE
ids = driver.find_elements_by_xpath("//*[@id]")
all_feat = []
for ii in ids:
    print(ii.get_attribute("id"))
driver.quit()
