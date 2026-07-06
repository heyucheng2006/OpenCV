import cv2

a=cv2.imread("001.bmp", cv2.IMREAD_UNCHANGED)
b=cv2.imread("002.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("demo", a)
cv2.imshow("demo2", b)

m=a[0:400, 300:600]
b[100:500, 400:700]=m

cv2.imshow("result", b)
cv2.waitKey(0)
cv2.destroyAllWindows()