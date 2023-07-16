#! /usr/bin/env python 

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("OpenCV/task12/image/04_LenaNoise.png")

# 中值滤波
img_median = cv2.medianBlur(img, 3)

# 均值滤波
img_blur = cv2.blur(img, (3, 3))

# 高斯滤波
img_gaussian = cv2.GaussianBlur(img, (3, 3), 1)

img_result = np.hstack((img, img_median, img_blur, img_gaussian))

cv2.imshow("Image", img_result)
cv2.waitKey(0)