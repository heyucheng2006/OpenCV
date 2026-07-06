import cv2
import numpy as np

a=cv2.imread("001.bmp",0)    #原始
r,c=a.shape
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)     #密钥图像，随机数生成
encryption=cv2.bitwise_xor(a,key)    #加密
decryption=cv2.bitwise_xor(encryption,key)    #解密 （a）

cv2.imshow("a",a)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey(0)
cv2.destroyAllWindows()
