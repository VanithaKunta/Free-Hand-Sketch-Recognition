#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:31:48 2022

@author: deva
"""

import cv2
import numpy as np

img = cv2.imread('/Users/Deva/Downloads/Dataset/airplane/2.png', 0)

kernel = np.ones((5, 5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imwrite("erosion_result.png", img_erosion)

cv2.waitKey(0)