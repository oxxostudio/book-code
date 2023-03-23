# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread('mona.jpg')
output = img    # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(img, output, alpha, beta)  # 套用 convertScaleAbs
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()
