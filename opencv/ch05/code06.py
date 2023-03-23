# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread('meme.jpg')
M = np.float32([[1, 0, 100], [0, 1, 100]]) # 2x3 矩陣，x 軸平移 100，y 軸平移 100
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)
