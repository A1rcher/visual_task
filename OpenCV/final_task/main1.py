#! /usr/bin/env python

import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread("OpenCV/final_task/image/1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化处理
_, thres = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

# 开运算，去除一些细小的连通域
thres = cv2.morphologyEx(thres,cv2.MORPH_OPEN, kernel)

# 寻找连通域的边缘，并将边缘像素点存储在contours列表中
contours, hierarchy = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 遍历contours，寻找边缘长度符合范围，并且为闭合的曲线，添加到新的列表contours_new
contours_new =[]
for contour in contours:
    if 95<cv2.arcLength(contour, True)<200:
        contours_new.append(contour)

# 根据contours_new, 以填充的方式画出边缘
cv2.drawContours(img,contours_new,-1,(0, 0,255),cv2.FILLED)

cv2.imshow("Image", img)
cv2.waitKey(0)