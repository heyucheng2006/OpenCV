import cv2
import numpy as np

img1=np.random.randint(0,256,size=[256,256],dtype=np.uint8)
img2=np.random.randint(0,256,size=[256,256],dtype=np.uint8)

print("img1=\n",img1)
print("img2=\n",img2)   
print("img1+img2=\n",img1+img2)

img3=cv2.add(img1,img2)
print("img3=\n",img3)   

cv2.imshow("img1",img1)
cv2.imshow("img2",img2) 
cv2.imshow("img1+img2",img1+img2)
cv2.imshow("img3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
