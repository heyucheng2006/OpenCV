import cv2
import numpy as np

a=cv2.imread("001.bmp",0)
cv2.imshow("a",a)

r,c=a.shape
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(a,x[:,:,i])
    mask=r[:,:,i]>0
    r[:,:,i][mask]=255
    cv2.imshow(str(i),r[:,:,i])

cv2.waitKey(0)
cv2.destroyAllWindows()