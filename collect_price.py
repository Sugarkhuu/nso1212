import pandas as pd
import pdb
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import datetime

chrome_options = Options() 
# chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

for i in range(1,60):
    print("page {}".format(i) )
    url = "https://1212.mn/mn/statistic/file-library/weekprice?page=" + str(i) # url for reports
    driver.get(url)
    time.sleep(5)
    # list of weekly reports in a page
    list = driver.find_elements(By.XPATH,"/html/body/app-root/div[1]/app-file-library/div/div[3]/div[2] \
                        /div/app-file-library-list/div[1]/div/div/div/p-table/div/div/table/tbody/tr")

    for file in list:

        file_type = file.find_element(By.XPATH,'td/div/div[3]/div[3]/span').text

        # take only xls(x) - pdf is too slow to download
        if 'x' in file_type: 
            file.find_element(By.XPATH,'td/div/div[1]').click()
            time.sleep(2)
            print("file {}".format(file) )
