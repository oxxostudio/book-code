# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
output1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img_gray2 = cv2.medianBlur(img_gray, 5)   # 模糊化
output2 = cv2.adaptiveThreshold(img_gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)
cv2.destroyAllWindows()
