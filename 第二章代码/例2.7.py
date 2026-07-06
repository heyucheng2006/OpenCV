import numpy as np

img = np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)

print("img=\n", img)
print("Element at (3, 2):", img.item(3, 2))

img[3,2] = 100
print("修改后 img=\n", img)
print("Element at (3, 2):", img.item(3, 2))
