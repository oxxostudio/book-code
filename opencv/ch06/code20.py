# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h,w,4), dtype='uint8')
a = 0                       # 開始時 a 等於 0
while True:

    key = cv2.waitKey(1)    # 偵測按鍵
    if key == 32:
        a = 1               # 如果按下空白鍵，讓 a 等於 1
    elif key == ord('q'):
        break

    if a == 0:
        output = img.copy() # 如果 a 等於 0，複製來源圖片為 output
    else:
        output = cv2.addWeighted(white, a, img, 1-a, 0)  # 如果 a 等於 1，根據 a 套用權重
        a = a - 0.01        # a 不斷減少 0.01
        if a<0: a = 0       # 如果 a 小於 0 就讓 a 等於 0

    cv2.imshow('oxxostudio', output)

cap.release()
cv2.destroyAllWindows()
