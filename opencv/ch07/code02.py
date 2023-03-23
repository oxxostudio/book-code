# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Sobel(img, -1, 1, 1, 1, 7)      # 偵測邊緣
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
