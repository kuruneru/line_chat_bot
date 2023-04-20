# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:16:09 2023

@author: takay
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import tkinter

root = tkinter.Tk()
root.geometry("300x400")
root.title("url")
textbox = tkinter.Entry()
text = textbox.get()

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.jalan.net")

browser_element_textbox = browser.find_element(By.ID, )
