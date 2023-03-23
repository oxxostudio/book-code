# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output1 = cv2.blur(img, (5, 5))     # 指定區域單位為 (5, 5)
output2 = cv2.blur(img, (25, 25))   # 指定區域單位為 (25, 25)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()
