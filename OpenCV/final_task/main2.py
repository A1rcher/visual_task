#! /usr/bin/env python

import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("OpenCV/final_task/image/2.jpg")
height, width, channel = img.shape
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化处理
_, thres = cv2.threshold(img_gray, 140, 255, cv2.THRESH_BINARY)

# 开运算，去除一些小噪点
thres = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel)

# 检测连通域边缘
contours, hierarchy = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 遍历contours，将面积大于指定范围的边缘，存储到新的列表中，即为所需要的区域
contours_new =[]
for contour in contours:
    if 1500<cv2.contourArea(contour):
        contours_new.append(contour)

# 创建一块黑色画布
mask = np.zeros((height, width, channel), np.uint8)

# 根据contours_new，在画布上画出连通域
cv2.drawContours(mask,contours_new,-1,(255,255,255),cv2.FILLED)

# 检测画布的连通域，并把外接矩阵的信息存储到stats中
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
num, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)

# 根据stats，画出外接矩阵
cv2.rectangle(img, (stats[1,0], stats[1,1]), (stats[1,0]+stats[1,2], stats[1,1]+stats[1,3]),(0, 255, 0), 2)

cv2.imshow("Iamge", img)
cv2.waitKey(0)