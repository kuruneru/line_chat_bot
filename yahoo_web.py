# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:36:59 2023

@author: takay
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://auctions.yahoo.co.jp/#")

browser_input = browser.find_element(By.XPATH, "//div[@class='InputTextArea-sc-m9wazc lohcAb']/div/input")
browser_input.send_keys("PCパーツ")

browser_input.send_keys(Keys.ENTER)

browser_check_button = browser.find_element(By.CLASS_NAME,"CheckBox")

browser_check_button.click()