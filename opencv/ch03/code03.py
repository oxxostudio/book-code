# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg', cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
cv2.imshow('oxxostudio', img)
cv2.waitKey(2000)       # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗
cv2.destroyAllWindows()
