import cv2
import numpy as np

a=cv2.imread("001.bmp")
b=np.zeros(a.shape,dtype=np.uint8)
b[100:400,200:400]=255
b[100:500,100:200]=255
c=cv2.bitwise_and(a,b)
d=cv2.bitwise_or(a,b)
e=cv2.bitwise_not(a)
f=cv2.bitwise_xor(a,b)

print("a.shape:",a.shape)
print("b.shape:",b.shape)
print("c.shape:",c.shape)
print("d.shape:",d.shape)
print("e.shape:",e.shape)
print("f.shape:",f.shape)

cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.imshow("d",d)
cv2.imshow("e",e)
cv2.imshow("f",f)

cv2.waitKey(0)
cv2.destroyAllWindows()
