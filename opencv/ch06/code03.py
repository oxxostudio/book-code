# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output1 = cv2.medianBlur(img, 5)   # 模糊程度為 5
output2 = cv2.medianBlur(img, 25)  # 模糊程度為 25
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)
cv2.destroyAllWindows()
