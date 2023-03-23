# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

logo = cv2.imread('logo.jpg')
size = logo.shape
img = np.zeros((360,600,3), dtype='uint8')
img[0:360, 0:600] = '255'
img[0:size[0], 0:size[1]] = logo
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask = mask1 )
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))   # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask = mask2 )
    output = cv2.add(bg, logo)
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
