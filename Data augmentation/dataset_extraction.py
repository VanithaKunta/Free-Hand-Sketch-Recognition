#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:07:48 2022

@author: deva
"""

import os

DATASET_PATH = r'/Users/Deva/Downloads/Dataset'

for roots, directories, files in os.walk(DATASET_PATH):
    for file in files:
        print("Path of directory ", roots)
        print("Filename ", file)
        print("Path of sample ", os.path.join(roots, file))
        print("Label ", roots.split('\\')[-1])

