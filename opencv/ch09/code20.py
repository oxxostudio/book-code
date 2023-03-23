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
    img = cv2.resize(img,(640,360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0,0,255)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)                      # 取得座標與長寬尺寸
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)  # 繪製四邊形

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
