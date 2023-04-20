import cv2

path = "C:\\Users\\takay\\OneDrive\\python_script\\IMG_0100.JPG"

cascade_path = './haarcascades/haarcascade_frontalface_alt.xml'

img = cv2.imread(path)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray",img_gray)
cv2.waitKey(0)

cascade = cv2.CascadeClassifier(cascade_path)

face_list = cascade.detectMultiScale(img_gray,minSize = (20,20))

if len(face_list):
    for (x,y,w,h) in face_list:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),thickness=3)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    
else:
    print("not found")