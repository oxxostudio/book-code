# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')   # 繪製 300x300 的黑色畫布
cv2.line(img,(50,50),(250,250),(0,0,255),5)  # 繪製線條
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()
