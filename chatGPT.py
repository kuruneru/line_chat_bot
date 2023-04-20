# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:58:47 2023

@author: takay
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriverの設定
driver = webdriver.Chrome()  # Chromeを使う場合

# じゃらんのトップページにアクセスする
driver.get('https://www.jalan.net/')

# 「宿泊予約」ボタンをクリックする
reserve_button = driver.find_element(By.XPATH, '//*[@id="srchBox"]/div[1]/div[3]/div[1]/a')
reserve_button.click()

# 「地域・ホテル名・旅館名・キーワード」欄に「釧路市」を入力する
area_input = driver.find_element(By.ID,'free_word')
area_input.send_keys('釧路市')

# 「検索」ボタンをクリックする
search_button = driver.find_element(By.ID,'searchButton')
search_button.click()

# 「朝食付き」にチェックを入れる
breakfast_checkbox = driver.find_element(By.ID,'breakfastSelect')
breakfast_checkbox.click()

# WebDriverを閉じる
driver.quit()