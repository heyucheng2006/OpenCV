import cv2
import numpy as np

a=cv2.imread("002.png",0)    #读取原始载体图像
watermark=cv2.imread("001.bmp",0)    #读取水印图像
#将水印缩放到和载体一样大
watermark=cv2.resize(watermark, (a.shape[1], a.shape[0]))
#将水印图像内的值255处理为1，方便嵌入
w=watermark[:,:]>0
watermark[w]=1
#读取原始载体图像的shape值
r,c=a.shape
#===========嵌入过程=========
#生成元素值都是254的矩阵
t254=np.ones((r,c),dtype=np.uint8)*254
#获取a的高7位
aH7=cv2.bitwise_and(a,t254)    #a的高7位
#讲watermark嵌入到aH7内
e=cv2.bitwise_or(watermark,aH7)    #嵌入水印
#============提取过程
#生成元素值都是1的矩阵
t1=np.ones((r,c),dtype=np.uint8)
#从载体图像内
wm=cv2.bitwise_and(e,t1)
print(wm)
#水印图像内的值1处理为255，方便显示
w=wm[:,:]>0
wm[w]=255
#============
cv2.imshow("a",a)
cv2.imshow("watermark",watermark)  
cv2.imshow("e",e)
cv2.imshow("wm",wm) 
cv2.waitKey(0)
cv2.destroyAllWindows() 