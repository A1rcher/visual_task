#! /usr/bin/env python

import cv2
import numpy as np

img = cv2.imread("OpenCV/task13/image/1.jpeg")
img = cv2.resize(img, (0, 0),fx=0.5, fy=0.5)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny边缘检测
img_can = cv2.Canny(img, 100, 255)

cv2.imshow("Image", img_can)
cv2.waitKey(0)