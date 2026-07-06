import cv2
import numpy as np

img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
mask=np.zeros((4,4),dtype=np.uint8)
mask[1:3,1:3]=1
img3=np.ones((4,4),dtype=np.uint8)*66

print("img1:\n",img1)
print("img2:\n",img2)
print("img3:\n",img3)

print("初始值img3=\n",img3)
img3=cv2.add(img1,img2,mask=mask)
print("加法后img3=\n",img3)