import cv2
import numpy as np

a=cv2.imread("001.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.imread("002.png",cv2.IMREAD_UNCHANGED)

cv2.imshow("a",a)
cv2.imshow("b",b)

face1=a[100:300,100:300]
face2=b[100:300,100:300]
add=cv2.addWeighted(face1,0.5,face2,0.5,4)
b[100:300,100:300]=add

cv2.imshow("result",b)
cv2.waitKey()   
cv2.destroyAllWindows()