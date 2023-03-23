# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
lower = np.array([30,40,200])   # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))           # 縮小尺寸，加快處理速度
    output = cv2.inRange(img, lower, upper)   # 取得顏色範圍的顏色
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(output, kernel)       # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)        # 縮小影像，還原大小

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
