import cv2

gray = cv2.imread("001.bmp", 0)
color = cv2.imread("001.bmp")

print("gray")
print("gray.shape=", gray.shape)
print("gray.size=", gray.size)
print("gray.dtype=", gray.dtype)

print("color")
print("color.shape=", color.shape)
print("color.size=", color.size)
print("color.dtype=", color.dtype)