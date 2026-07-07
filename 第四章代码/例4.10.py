import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#=============指定肤色的H通道范围=============
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)

#=============指定肤色的S通道范围=============
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)

#=============合并H通道和S通道的掩码=============
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("img", img)
cv2.imshow("ROI", roi)

cv2.waitKey()
cv2.destroyAllWindows()
