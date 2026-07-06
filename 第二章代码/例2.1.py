import cv2
import numpy as np

img = np.zeros((8,8),dtype=np.uint8)
img[0,3]=255
print(img)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()