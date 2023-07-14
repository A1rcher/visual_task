#! /usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel_size = [3, 5, 7, 9]
for i in kernel_size:
    kernel = np.ones((i, i), np.uint8)

    img = cv2.imread("OpenCV/task09/image/9.png", cv2.IMREAD_GRAYSCALE)

    # 腐蚀
    img_ero = cv2.erode(img, kernel,iterations=1)

    # 膨胀
    img_dil = cv2.dilate(img, kernel, iterations=1)

    # 开运算: 先腐蚀，后膨胀
    img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # 闭运算: 先膨胀，后腐蚀
    img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    fig = plt.figure()
    fig.canvas.manager.set_window_title(f"kernel size: {i}")

    plt.subplot(231), plt.imshow(img, 'gray'), plt.title("Origin")
    plt.subplot(232), plt.imshow(img_ero, 'gray'), plt.title("Erode")
    plt.subplot(233), plt.imshow(img_dil, 'gray'), plt.title("Dilate")
    plt.subplot(234), plt.imshow(img_open, 'gray'), plt.title("Open")
    plt.subplot(235), plt.imshow(img_close, 'gray'), plt.title("Close")

    plt.show()
