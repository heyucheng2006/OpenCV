import cv2
import numpy as np

a=cv2.imread("001.bmp")
b=cv2.imread("002.png")
c=cv2.resize(b,(a.shape[1],a.shape[0]))   #只有把两张图片的大小尺寸统一才可以加权
result=cv2.addWeighted(a,0.3,c,0.7,2)

cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()