import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("img.shape=", img.shape)
print("rgb.shape=", rgb.shape)
print("原图像素点(0,0) BGR=", img[0, 0])
print("转换后像素点(0,0) RGB=", rgb[0, 0])

cv2.imshow("img", img)
cv2.imshow("rgb", rgb)

cv2.waitKey()
cv2.destroyAllWindows()
