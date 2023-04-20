# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:21:17 2022

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
   textbox2.delete(0,tkinter.END)
   number = int(textbox1.get())
   quotient_list = []
   for i in range(1,number+1):
       if (number / i).is_integer() == True:
           quotient_list.append(str(round(number / i)))
        
        
   for n in quotient_list:
       if int(n) == number:
            x = 1
    
       elif int(n) == 1:
            x += 1
            
       else:
            x = 0
        
   if x == 2:
        textbox2.insert(tkinter.END,"この数は素数です")
        
        
   elif x == 1:
        textbox2.insert(tkinter.END,"この数は素数ではありません")

    

button = tkinter.Button(text="classification",command=PRIME_NUMBER_CLASSIFICATION)
button.pack()

root.mainloop()