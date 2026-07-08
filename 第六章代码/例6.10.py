import cv2

img = cv2.imread("001.bmp", 0)
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

print("t=", t)
cv2.imshow("img", img)
cv2.imshow("rst", rst)
cv2.waitKey()
cv2.destroyAllWindows()

