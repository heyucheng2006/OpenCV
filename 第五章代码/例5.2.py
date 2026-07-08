import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

rows, cols = img.shape[:2]
size = (int(cols * 0.9), int(rows * 0.5))
rst = cv2.resize(img, size)

print("img.shape=", img.shape)
print("rst.shape=", rst.shape)

cv2.imshow("img", img)
cv2.imshow("resize", rst)
cv2.waitKey()
cv2.destroyAllWindows()

