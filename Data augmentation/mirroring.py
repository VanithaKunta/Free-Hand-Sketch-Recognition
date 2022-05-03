#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:14:48 2022

@author: deva
"""

import cv2
import numpy as np

img = cv2.imread('/Users/Deva/Downloads/Dataset/airplane/2.png', 0)
cv2.imshow("original", img)

horizontal_inverted_img = cv2.flip(img, 1)
cv2.imshow("mirrored", horizontal_inverted_img)
cv2.imwrite("mirrored_result.png", horizontal_inverted_img)

cv2.waitKey(0)
