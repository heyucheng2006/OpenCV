"""
第一个 OpenCV Demo —— 显示图片、画图、认识基本操作
"""
import cv2
import numpy as np

# ========= 1. 创建一张纯色背景图 =========
img = np.zeros((400, 600, 3), dtype=np.uint8)  # 黑色画布 (高400, 宽600)
img[:] = (50, 50, 50)  # 深灰色背景 (B, G, R)

# ========= 2. 画一些图形 =========
cv2.rectangle(img, (50, 50), (250, 200), (0, 255, 0), 3)   # 绿色矩形
cv2.circle(img, (400, 125), 75, (255, 0, 0), -1)            # 蓝色实心圆
cv2.line(img, (50, 300), (550, 300), (0, 0, 255), 5)         # 红色横线
cv2.putText(img, 'Hello OpenCV!', (120, 350),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)  # 白色文字

# ========= 3. 显示信息 =========
print(f"OpenCV 版本: {cv2.__version__}")
print(f"图片尺寸: {img.shape} (高, 宽, 通道)")
print(f"图片大小: {img.size} 像素")
print(f"数据类型: {img.dtype}")

# ========= 4. 保存并显示 =========
cv2.imwrite('demo_output.jpg', img)
print("图片已保存: F:\\OpenCV\\demo_output.jpg")
print("请打开该文件查看效果！")
