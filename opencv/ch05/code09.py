# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

p1 = np.float32([[100,100],[480,0],[0,360],[480,360]])
p2 = np.float32([[0,0],[480,0],[0,360],[480,360]])
m = cv2.getPerspectiveTransform(p1,p2)

img = cv2.imread('meme.jpg')
output = cv2.warpPerspective(img, m, (480, 360))
cv2.imshow('oxxostudio', output)
