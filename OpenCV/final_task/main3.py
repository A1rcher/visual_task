#! /usr/bin/env python

import cv2
import numpy as np

lowerb = (14, 4, 75)
upperb = (90, 93, 180)

kernel = np.ones((3, 3), np.uint8)

img = cv2.imread("OpenCV/final_task/image/3.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
thres = cv2.inRange(img_hsv, lowerb, upperb)
thres = cv2.dilate(thres, kernel, iterations=3)
thres = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel)



cv2.imshow("Image", img)
cv2.imshow("result", thres)
cv2.waitKey(0)