# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:44:27 2023

@author: takay
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\takay\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='gb']/div/div[2]/div[2]/div/a").click()
time.sleep(3)

driver.close()