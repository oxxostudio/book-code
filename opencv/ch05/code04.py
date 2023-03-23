# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output_1 = cv2.resize(img, (200, 200))   # 產生 200x200 的圖
output_2 = cv2.resize(img, (100, 300))   # 產生 100x300 的圖
cv2.imwrite('output_1.jpg', output_1)
cv2.imwrite('output_2.jpg', output_2)
