import cv2
img = cv2.imread("001.bmp",0)
for i in range(10,100):
    for j in range(80,100):
        img[i,j]=0 
#img[10:100, 80:100] = 255
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()