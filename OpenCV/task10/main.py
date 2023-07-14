#! /usr/bin/env python 

import cv2
import numpy as np

# 读取图像，并生成一张同尺寸的画布
img = cv2.imread("OpenCV/task10/image/10.png")
height, width, channel = img.shape
img_out = np.zeros((height, width, channel), np.uint8)

# 计算连通域，num：连通域的数量 labels：每个像素的标记 stats：存储外接矩阵的信息 centroids：存储每个连通域的中心坐标
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_thres = cv2.threshold(img_gray, 85, 255, cv2.THRESH_BINARY)  # 二值处理
num, labels, stats, centroids = cv2.connectedComponentsWithStats(img_thres)

# 生成一个包含连通域数目的随机颜色矩阵
color_list = [[0, 0, 0]]
for i in range(num-1):
    color = np.random.randint(0, 255, 3, dtype=np.uint8)
    color_list.append(color)

# 遍历像素，根据labels的标记，给每个像素赋值
for i in range(height):
    for j in range(width):
        img_out[i, j] = color_list[labels[i, j]] 

# 用外接矩阵框出连通域
for stat in stats[1:]:
    cv2.rectangle(img_out, (stat[0], stat[1]), (stat[0]+stat[2], stat[1]+stat[3]), (0, 255, 0), 1)

# 打印连通域的数量
print(f"连通域的数量:{num}")

cv2.imshow("Image", img_out)
cv2.waitKey(0)