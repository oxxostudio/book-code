# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg', cv2.IMREAD_GRAYSCALE)   # 以灰階模式開啟圖片
cv2.imwrite('oxxostudio_2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
cv2.imwrite('oxxostudio_3.png', img)  # 存成 png
