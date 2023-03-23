# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
M = cv2.getRotationMatrix2D((240, 180), 45, 1)    # 中心點 (240, 180)，旋轉 45 度，尺寸 1
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)
