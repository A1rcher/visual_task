#! /usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('OpenCV/task_1/image/1.jpg')   # 读取图片
height, width, _ = img.shape
for row in range(height):
    for col in range(width):
        average = sum(img[row, col]) // 3       # 计算(b+g+r)/3的值
        img[row, col] = [average, average, average]     # 改变像素值

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print('average:',img[0,:10,0])
# print('gray:   ',img_gray[0,:10])
# cv2.imshow('Image_Gray', img_gray)
cv2.imshow('Image', img)            # 输出图像
cv2.waitKey(0)






