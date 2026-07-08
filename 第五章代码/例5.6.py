import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((width / 2, height / 2), -45, 0.8)
#第二个值为正（45），逆时针旋转；顺时针则是负值
rotate = cv2.warpAffine(img, M, (width, height))

cv2.imshow("original", img)
cv2.imshow("rotation", rotate)
cv2.waitKey()
cv2.destroyAllWindows()

