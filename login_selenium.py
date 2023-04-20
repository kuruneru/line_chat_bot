# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 00:30:57 2023

@author: takay
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--headless")
user_name = "imanishi"
password = "kohei"

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

user_name_element = browser.find_element(By.ID, "username")
user_name_element.send_keys(user_name)

password_element = browser.find_element(By.ID, "password")
password_element.send_keys(password)

login_botton = browser.find_element(By.ID, "login-btn")
login_botton.click()

browser.quit()