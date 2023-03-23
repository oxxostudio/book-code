# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

img = cv2.imread('mona.jpg')                         # 開啟圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)          # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = img.shape[1]                                     # 取得寬度
h = img.shape[0]                                     # 取得高度
white = 255 - np.zeros((h,w,4), dtype='uint8')       # 建立白色圖
a = 1                                                # 一開始 a 為 1
while True:
    a = a - 0.01                                     # a 不斷減少 0.01
    if a<0: a = 0                                    # 如果 a 小於 0 就讓 a 等於 0
    output = cv2.addWeighted(white, a, img, 1-a, 0)  # 根據 a 套用權重
    cv2.imshow('oxxostudio', output)                 # 顯示圖片
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗
