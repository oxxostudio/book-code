# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')   # 開啟圖片
output_0 = cv2.flip(img, 0)    # 上下翻轉
output_1 = cv2.flip(img, 1)    # 左右翻轉
output_2 = cv2.flip(img, -1)   # 上下左右翻轉
cv2.imwrite('meme_0.jpg', output_0)
cv2.imwrite('meme_1.jpg', output_1)
cv2.imwrite('meme_2.jpg', output_2)
