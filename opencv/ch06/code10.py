# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
output = np.zeros((360,640,3), dtype='uint8')   # 產生 640x360 的黑色背景

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640, 360))   # 改變影像尺寸為 640x360
    img = img[:360, :320]               # 取出 320x360 的影像
    img2 = cv2.flip(img, 1)             # 左右翻轉影像
    output[:, :320] = img               # 將 output 左邊內容換成 img
    output[:, 320:640] = img2           # 將 output 右邊內容換成 img2

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
