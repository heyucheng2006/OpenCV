import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#=============调整HSV色彩空间内V通道的值=============
v[:, :] = 128
newHSV = cv2.merge([h, s, v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

cv2.imshow("img", img)
cv2.imshow("art", art)

cv2.waitKey()
cv2.destroyAllWindows()
