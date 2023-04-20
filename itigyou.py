# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:19:38 2022

@author: takay
"""

import pandas as pd
#読み込むファイルのリスト
file_list = ["cor_hw.xlsx","book.xlsx"]
#Excelデータを蓄積するリスト
date_list = []
#ファイルを読み込むループを作成
for Excel_filename in file_list:
    #Excelデータの読み込み
    df = pd.read_excel(Excel_filename)
    #行でループを繰り返す
    for index , rows in df.iterrows():
        #一行分のデータを保存するリストを作成
        work = []
        #行ループ
        for col in rows:
            #一行分データをリストに追加
            date_list.append(work)
#最後に読み込んだファイルからExcelファイルから列名を取得
columns = list(df.columns)
#データリストにもとのデータフレームを作成
df = pd.DataFrame(date_list, columns=columns)
with pd.ExcelWriter("data.xlxs") as writer:
    df.to_excel(writer,index=False)
    
    