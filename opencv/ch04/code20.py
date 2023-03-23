# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式
print(img.shape)                             # (400, 300, 4)  第三個數值變成 4
