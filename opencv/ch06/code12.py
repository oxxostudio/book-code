# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)                      # 讀取攝影鏡頭
output = np.zeros((360,640,3), dtype='uint8')  # 產生 640x360 的黑色背景

if not cap.isOpened():
    print("Cannot open camera")
    exit()

n = 5                                  # 設定要分成幾格
w = 640//n                             # 計算分格之後的影像寬度 ( // 取整數 )
h = 360//n                             # 計算分格之後的影像高度 ( // 取整數 )
while True:
    ret, img = cap.read()              # 讀取影像
    img = cv2.resize(img,(w, h))       # 縮小尺寸
    output[0:h, 0:w] = img             # 將 output 的特定區域置換為 img
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
