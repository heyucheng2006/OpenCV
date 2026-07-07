import cv2

img = cv2.imread("001.bmp")
if img is None:
    raise FileNotFoundError("没有找到图片：001.bmp")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

print("img.shape=",img.shape)
print("gray.shape=\n",gray.shape)
print("bgr.shape=",bgr.shape)
  
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("bgr", bgr)

cv2.waitKey()
cv2.destroyAllWindows()
