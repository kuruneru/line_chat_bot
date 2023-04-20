import cv2
import tkinter
import os
x = 0

#ウィンドウ作成
root = tkinter.Tk()
root.title("アプリ")
root.geometry("750x300")

#テキストボックスの作成とリスト化
textbox = tkinter.Entry(width=100)
textbox.place(x=90,y=70)

textbox2 = tkinter.Entry(width=20)
textbox2.place(x=300,y=200)

#関数の定義
def application():
    global x
    global height
    global width
    global img
    path = textbox.get()
    path_list = path.split(",")
    specify_size = int(textbox2.get())
    #一つずつファイルのサイズを足していって合計のファイルサイズの変数totalsizeに入れていく
    for path_number in path_list:
        abs_path = os.path.abspath(path_number)
        size = os.path.getsize(abs_path)
        totalsize =+ size
    while(totalsize > specify_size):
        for number_path in path_list:
            abspath = os.path.abspath(number_path)
            img = cv2.imread(abspath)
            height = img.shape[0]
            width = img.shape[1]
            resize = cv2.resize(img,dsize=(height,width))
    print('succece!')
    print(totalsize)

 #ボタンの作成
button = tkinter.Button(root,text="use",command=application)

button.pack()

root.mainloop()