import cv2
import tkinter
import os
x = 0

#ウィンドウ作成
root = tkinter.Tk()
root.title("アプリ")
root.geometry("750x100")

#テキストボックスの作成とリスト化
textbox = tkinter.Entry(width=100)
textbox.place(x=90,y=70)

#関数の定義
def application():
    global x
    global height
    global width
    global img
    path = textbox.get()
    path_list = path.split(",")
    for number_path in path_list:
        abspath = os.path.abspath(number_path)
        size = os.path.getsize(abspath)
        img = cv2.imread(abspath)
        x += 1
        height = img.shape[0]
        width = img.shape[1]
        while(size > 200):
            height -= 1
            width -= 1
            resize = cv2.resize(img,dsize=(width,height))
            cv2.imwrite(f"resize{x}.jpg",resize)
            cv2.imshow("resize",img)
    print('succece!')        

 #ボタンの作成
button = tkinter.Button(root,text="use",command=application)

button.pack()

root.mainloop()