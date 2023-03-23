# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('girl.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()
