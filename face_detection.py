import cv2

path = "C:\\Users\\takay\\OneDrive\\python_script\\IMG_0100.JPG"

#学習モデルのパス
cascade_path = "C:\\Users\\takay\\OneDrive\\python_script\\haarcascades\\haarcascade_frontalface_alt.xml"
img = cv2.imread(path)
#画像処理のノイズ除去のため一旦グレースケールに変更
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#グレープスケールの表示
cv2.imshow("img",img_gray)
cv2.waitKey(0)

#学習モデルの読み込み
cascade = cv2.CascadeClassifier(cascade_path)

#顔の検出
#minSizeで最小検出サイズを指定
face_list = cascade.detectMultiScale(img_gray, minSize=(20,20))

#顔が見つかるまで条件分岐
if len(face_list):
    for (x,y,w,h) in face_list:
        #顔が見つかった場合赤い四角で囲う
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),thickness=3)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    
#顔が見つからなかった場合
else:
    print("見つかりませんでした")