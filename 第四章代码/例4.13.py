import cv2

img = cv2.imread("003.png")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

#=============为BGR图像添加alpha通道=============
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)

#=============将alpha通道的值设置为125=============
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])

#=============将alpha通道的值设置为0=============
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

cv2.imshow("img", img)
cv2.imshow("bgra", bgra)
cv2.imshow("bgra125", bgra125)
cv2.imshow("bgra0", bgra0)

cv2.waitKey()
cv2.destroyAllWindows()
