# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread('meme.jpg')
p1 = np.float32([[100,100],[480,0],[0,360]])
p2 = np.float32([[0,0],[480,0],[0,360]])
M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)
