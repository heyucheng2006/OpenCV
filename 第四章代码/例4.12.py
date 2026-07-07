import cv2
import numpy as np

img = np.random.randint(0, 256, size=[2, 3, 3], dtype=np.uint8)

#=============将BGR图像转换为BGRA图像=============
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print("img=\n", img)
print("bgra=\n", bgra)

#=============分析alpha通道的值=============
b, g, r, a = cv2.split(bgra)
print("a=\n", a)

#=============修改alpha通道的值=============
a[:, :] = 125
bgra = cv2.merge([b, g, r, a])
print("bgra=\n", bgra)
