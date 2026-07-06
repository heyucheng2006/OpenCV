import cv2
import numpy as np

a=cv2.imread("002.png", -1)
b=a
result1=a+b       #numpy数组的取模效果
result2=cv2.add(a,b)    #亮度增加，图像叠加
result3=a+result1

cv2.imshow("a",a)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.imshow("result3",result3)
cv2.waitKey()
cv2.destroyAllWindows()