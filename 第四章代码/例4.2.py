import cv2
import numpy as np

img = np.random.randint(0, 256, size=[2, 4], dtype=np.uint8)
rst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

print("img=\n", img)
print("rst=\n", rst)
print("img shape=", img.shape)
print("rst shape=", rst.shape)
print("像素点（1,0）的灰度值=", img[1, 0])
print("像素点（1,0）转换后的BGR值=", rst[1, 0])

