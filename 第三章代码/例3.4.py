import cv2
import numpy as np

img1=np.ones((4,4),dtype=np.uint8)*100
img2=np.ones((4,4),dtype=np.uint8)*50
gamma=3
img3=cv2.addWeighted(img1,0.4,img2,0.6,gamma)

print("img3=\n",img3)