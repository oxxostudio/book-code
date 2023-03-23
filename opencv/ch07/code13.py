# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

logo = cv2.imread('logo.jpg')
size = logo.shape
img = np.zeros((360,600,3), dtype='uint8')
img[0:360, 0:600] = '255'
img[30:30+size[0], 155:155+size[1]] = logo         # 將 logo 置中
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))
    output = cv2.bitwise_not(frame, mask = mask1 )      # 套用 not 和遮罩
    output = cv2.bitwise_not(output, mask = mask1 )     # 再次套用 not 和遮罩，將色彩轉成原來的顏色
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
