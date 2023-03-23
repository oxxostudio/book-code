# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('cars.jpg')                    # 讀取街道影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像

car = cv2.CascadeClassifier("haarcascade_fullbody.xml")    # 讀取人體模型
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
cars = car.detectMultiScale(gray, 1.1, 3)       # 偵測行人
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
