#! /usr/bin/env python

import cv2
import numpy as np

threshold = 100

img = cv2.imread('OpenCV/task_3/image/1.jpeg')
deep_img = img.copy()
shallow_img = img
height, width, _ = img.shape
for row in range(height):
    for col in range(width):
        average = sum(img[row, col])//3
        # 二值处理
        if average > threshold:
            average = 255
        else:
            average = 0
        
        img[row, col] = [average, average, average]


cv2.imshow('Image', img)
cv2.imshow('DeepImage', deep_img)
cv2.imshow('ShallowImage', shallow_img)
cv2.waitKey(0)