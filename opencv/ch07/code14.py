# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

mask = np.zeros((300,300,3), dtype='uint8')      # 建立 300x300 的黑色畫布
cv2.circle(mask,(150,150),100,(255,255,255),-1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)       # 進行高斯模糊

cv2.imshow('oxxostudio', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
