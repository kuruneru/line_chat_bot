# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:24:18 2023

@author: takay
"""

import requests
from bs4 import BeautifulSoup

url = "https://scraping-for-beginner.herokuapp.com/"
responce = requests.get(url)

soup = BeautifulSoup(responce.text,"html.parser")
print(soup)