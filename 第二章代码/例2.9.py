import cv2
import numpy as np

img = cv2.imread("001.bmp", 0)
print("读取像素点img[3,2]=", img[3, 2])
img[3, 2] = 100
print("修改后像素点img[3,2]=", img[3, 2])

cv2.imshow("before",img)
for i in range(12,100):
    for j in range(12,100):
        img[i,j] = 128
cv2.imshow("after", img)
cv2.waitKey(0)
cv2.destroyAllWindows()