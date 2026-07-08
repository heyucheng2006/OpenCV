import cv2
import numpy as np

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

rows, cols = img.shape[:2]
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)

for i in range(rows):
    for j in range(cols):
        mapx[i, j] = cols - 1 - j
        mapy[i, j] = i

rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow("original", img)
cv2.imshow("result", rst)
cv2.waitKey()
cv2.destroyAllWindows()

