import cv2

img = cv2.imread("001.bmp", 0)
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print("普通阈值 t1=", t1)
print("Otsu 自动阈值 t2=", t2)
cv2.imshow("img", img)
cv2.imshow("thd", thd)
cv2.imshow("otsu", otsu)
cv2.waitKey()
cv2.destroyAllWindows()

