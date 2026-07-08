import cv2
import numpy as np

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

rows, cols = img.shape[:2]
pts1 = np.float32([
    [cols * 0.30, rows * 0.10],
    [cols * 0.78, rows * 0.12],
    [cols * 0.18, rows * 0.88],
    [cols * 0.65, rows * 0.82],
])
pts2 = np.float32([
    [cols * 0.15, rows * 0.15],
    [cols * 0.85, rows * 0.15],
    [cols * 0.15, rows * 0.85],
    [cols * 0.85, rows * 0.85],
])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

