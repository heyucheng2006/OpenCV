import cv2

img = cv2.imread("001.bmp", 0)
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
athd_mean = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3
)
athd_gaus = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3
)

print("普通阈值 t=", t1)
cv2.imshow("img", img)
cv2.imshow("thd", thd)
cv2.imshow("athd_mean", athd_mean)
cv2.imshow("athd_gaus", athd_gaus)
cv2.waitKey()
cv2.destroyAllWindows()

