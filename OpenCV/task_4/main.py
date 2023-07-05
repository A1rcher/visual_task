#! /usr/bin/env python

import cv2

img = cv2.imread('OpenCV/task_4/image/1.jpeg')
img_b = img[:,:,0]
img_g = img[:,:,1]
img_r = img[:,:,2]
cv2.imshow('Image', img)
cv2.imshow('BlueImage', img_b)
cv2.imshow('GreenImage', img_g)
cv2.imshow('RedImage', img_r)
cv2.waitKey(0)