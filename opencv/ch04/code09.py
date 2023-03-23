# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
output3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('oxxostudio', img)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
cv2.waitKey(0)
cv2.destroyAllWindows()
