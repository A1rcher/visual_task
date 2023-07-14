#! /usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# gamma处理
def GammaChange(img, g=2.2):
    img_g = img.copy()
    img_g = img_g.astype(np.float64)
    img_g /= 255
    img_g = img_g ** (1/g)
    img_g *= 255
    img_g = img_g.astype(np.uint8)
    return img_g

img = cv2.imread("OpenCV/task07/image/7-1.png", cv2.IMREAD_GRAYSCALE)

img_g = GammaChange(img)    # 对图像进行Gamma矫正

plt.subplot(121), plt.imshow(img, 'gray'), plt.title("Origin")
plt.subplot(122), plt.imshow(img_g, 'gray'), plt.title("Gamma")
plt.show()
