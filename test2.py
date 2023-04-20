import ntpath
import os
import cv2

print(ntpath.sep)

file_path = "sabotender.jpg"
file_path2 = r"C:\Users\takay\OneDrive\python_script\sabotender.jpg"
abspath = os.path.abspath(file_path)
size = os.path.getsize(file_path2)
size2 = os.path.getsize(abspath)
print(size)
print(size2)
print(file_path2)
print(abspath)

img1 = cv2.imread(abspath)
img2 = cv2.imread(file_path2)

cv2.imshow("application1",img1)
cv2.waitKey(0)
cv2.imshow("application2",img2)
cv2.waitKey(0)