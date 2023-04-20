# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:54:39 2023

@author: takay
"""

import tkinter

hokkaidou = ["北海道"]
touhoku = ["青森","秋田","岩手","福島","宮城","山形"]
kitakantou = ["群馬","栃木","茨城"]
kousinshu = ["山梨","長野","新潟"]
shutoken = ["東京","神奈川","千葉","埼玉"]
hokuriku = ["富山","石川","福井"]
kinki = ["兵庫","大阪","和歌山","京都","奈良","滋賀","大阪"]
toukai = ["静岡","岐阜","愛知","三重"]
sanyou_sanin = ["広島","鳥取","島根","岡山","山口"]
sikoku = ["香川","徳島","愛媛","高知"]
kyushu = ["福岡","佐賀","長崎","熊本","大分","宮崎","鹿児島"]
okinawa = ["沖縄"]

sougou = [hokkaidou,touhoku,kitakantou,kousinshu,shutoken,hokuriku,kinki,toukai,sanyou_sanin,sikoku,kyushu,okinawa]

root = tkinter.Tk() 
root.geometry("300x400")
root.title("都道府県を選んでください")