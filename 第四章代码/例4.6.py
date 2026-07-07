import cv2
import numpy as np

#=========测试一下OpenCV中蓝色的HSV模式值=============
imgBlue = np.zeros([1, 1, 3], dtype=np.uint8)
imgBlue[0, 0, 0] = 255
blueHSV = cv2.cvtColor(imgBlue, cv2.COLOR_BGR2HSV)
print("Blue=\n", imgBlue)
print("BlueHSV=\n", blueHSV)
print("H={}, S={}, V={}".format(blueHSV[0,0,0], blueHSV[0,0,1], blueHSV[0,0,2]))

#=========测试一下OpenCV中绿色的HSV模式值=============
imgGreen = np.zeros([1, 1, 3], dtype=np.uint8)
imgGreen[0, 0, 1] = 255
greenHSV = cv2.cvtColor(imgGreen, cv2.COLOR_BGR2HSV)
print("Green=\n", imgGreen)
print("GreenHSV=\n", greenHSV)
print("H={}, S={}, V={}".format(greenHSV[0,0,0], greenHSV[0,0,1], greenHSV[0,0,2]))

#=========测试一下OpenCV中红色的HSV模式值=============
imgRed = np.zeros([1, 1, 3], dtype=np.uint8)
imgRed[0, 0, 2] = 255
redHSV = cv2.cvtColor(imgRed, cv2.COLOR_BGR2HSV)
print("Red=\n", imgRed)
print("RedHSV=\n", redHSV)
print("H={}, S={}, V={}".format(redHSV[0,0,0], redHSV[0,0,1], redHSV[0,0,2]))
