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
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    mask = cv2.inRange(frame, lower, upper)               # 使用 inRange
    output = cv2.bitwise_and(frame, frame, mask = mask )  # 套用影像遮罩
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
