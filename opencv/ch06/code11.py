# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
output = np.zeros((640,640,3), dtype='uint8')

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    img = cv2.resize(img,(640, 360))
    img = img[:320, :320]             # 取出 320x320 的區域
    img2 = cv2.flip(img, 1)           # 左右翻轉
    img3 = cv2.flip(img, 0)           # 上下翻轉
    img4 = cv2.flip(img, -1)          # 上下左右翻轉
    output[:320, :320] = img          # 左上
    output[:320, 320:640] = img2      # 右上
    output[320:640, :320] = img3      # 左下
    output[320:640, 320:640] = img4   # 右下

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

