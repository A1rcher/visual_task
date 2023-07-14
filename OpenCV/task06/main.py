#! /usr/bin/env python

import cv2
import numpy as np

img = np.zeros([400, 400, 3], np.uint8)
img[:] = [255, 255, 255]

cv2.rectangle(img, (100, 100), (150,150), (255, 0, 0), 3)
cv2.circle(img, (200, 200), 50, (0, 255, 0), cv2.FILLED)
cv2.line(img, (100, 100), (150, 150), (0, 0, 255), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)