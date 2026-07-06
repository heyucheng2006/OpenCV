import numpy as np
import cv2

img = np.random.randint(0, 256, size=[300, 300, 3], dtype=np.uint8)
print("img.shape=", img.shape)

# 用 for 循环将中间 10x10 区域设为蓝色 (B=255, G=0, R=0)
for i in range(5, 100):
    for j in range(60, 200):
        for k in range(0,3):
           img[i, j, 0] = 255  # B      
           img[i, j, 1] = 0    # G
           img[i, j, 2] = 0    # R     

print("修改完成，中间区域已设为蓝色")
cv2.imshow("demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()