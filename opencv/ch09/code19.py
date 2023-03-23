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

    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)    # 取得範圍內的面積
        color = (0,0,255)                  # 設定外框顏色
        # 如果面積大於 300 再標記，避免標記到背景中太小的東西
        if(area > 300):
            for i in range(len(contour)):
                if i>0 and i<len(contour)-1:
                    # 從第二個點開始畫線
                    img = cv2.line(img, (contour[i-1][0][0], contour[i-1][0][1]), (contour[i][0][0], contour[i][0][1]), color, 3)
                elif i == len(contour)-1:
                    # 如果是最後一個點，與第一個點連成一線
                    img = cv2.line(img, (contour[i][0][0], contour[i][0][1]), (contour[0][0][0], contour[0][0][1]), color, 3)

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
