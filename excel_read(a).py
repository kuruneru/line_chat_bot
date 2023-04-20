# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:05:33 2022

@author: takay
"""

import pandas as pd

df = pd.read_excel("book.xlsx")
read_data = pd.read_excel("cor_hw.xlsx",engine="openpyxl")
df = pd.concat([df,read_data])
with pd.ExcelWriter("book.xlsx") as writer:
    df.to_excel(writer,index=False)