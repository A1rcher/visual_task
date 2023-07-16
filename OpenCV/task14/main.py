#! /usr/bin/env python 

import cv2
import numpy as np

img = cv2.imread("OpenCV/task14/image/14-1.jpg")

# 双边滤波
img_blur = cv2.bilateralFilter(img, 7, 50, 70)


cv2.imshow("Image", img)
cv2.imshow("Image_", img_blur)
cv2.waitKey(0)