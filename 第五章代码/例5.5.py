import cv2
import numpy as np

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

height, width = img.shape[:2]
x = 700
y = 400
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(img, M, (width, height))

cv2.imshow("original", img)
cv2.imshow("move", move)
cv2.waitKey()
cv2.destroyAllWindows()

