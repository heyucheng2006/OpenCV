import cv2
import numpy as np

a=cv2.imread("001.bmp", cv2.IMREAD_UNCHANGED)
cv2.imshow("demo", a)

face=a[0:400, 300:600]
eye=np.random.randint(0, 256, (200,300,3))
cv2.imshow("face", face)

a[100:300, 400:700]=eye

cv2.imshow("result", a)
cv2.waitKey(0)
cv2.destroyAllWindows()