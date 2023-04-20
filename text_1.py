# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:56:49 2022

@author: takay
"""

import tkinter

root = tkinter.Tk()
root.title("APPLICATION")
root.geometry("500x200")
lbl = tkinter.Label(text="number=")
lbl.place(x=30,y=100)
textbox1 = tkinter.Entry(width=50)
textbox1.place(x=100,y=100)
textbox2 = tkinter.Entry(width=30)
textbox2.place(x=220,y=150)

def PRIME_NUMBER_CLASSIFICATION():
    number = int(textbox1.get())
    quotient_list = []
    for i in range(1,number+1):
        if (number / i).is_integer() == True:
            quotient_list.append(str(round(number / i)))
            print(quotient_list)
        
        
    for n in quotient_list:
        print(n)
        print(number)
        if int(n) == number:
            x = 1 
        elif int(n) == 1:
            x += 1
        else:
            x = -1
    print(x)
    if x == 2:
        print("OK")
        
    elif x == 1:
        print("NO")
        
    
        
BUTTON = tkinter.Button(text="CLASSIFICATION",command=PRIME_NUMBER_CLASSIFICATION)
BUTTON.pack()

root.mainloop()