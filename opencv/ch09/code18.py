# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
lower = np.array([30,40,200])
upper = np.array([90,100,255])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列，cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 使用 for 迴圈印出座標長相
    for contour in contours:
        print(contour)

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
