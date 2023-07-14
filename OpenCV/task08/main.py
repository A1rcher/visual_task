#! /usr/bin/env python

import cv2
import numpy as np

lowerb = (0, 50, 50)
upperb = (10, 255, 255)

img = cv2.imread("OpenCV/task08/image/8.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      # 转换成HSV色彩空间
mask = cv2.inRange(img_hsv, lowerb, upperb)    # 使用inRange函数创建出一个掩码
img_r = cv2.bitwise_and(img, img, mask=mask)    # 位与运算

# cv2.imshow("Image", img)
cv2.imshow("ImageR", img_r)
cv2.waitKey(0)