# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
cv2.waitKey(0)
cv2.destroyAllWindows()
