# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # 載入人臉偵測模型
faces = face_cascade.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()
