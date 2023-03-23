# Copyright © https://steam.oxxostudio.tw

import cv2
cap1 = cv2.VideoCapture(0)           # 讀取第一個影片來源
cap2 = cv2.VideoCapture(1)           # 讀取第二個影片來源

if not cap1.isOpened():
    print("Cannot open camera1")
    exit()
if not cap2.isOpened():
    print("Cannot open camera2")
    exit()

while True:
    ret1, img1 = cap1.read()         # 讀取第一個來源影片的每一幀
    ret2, img2 = cap2.read()         # 讀取第一個來源影片的每一幀

    cv2.imshow('oxxostudio1', img1)  # 如果讀取成功，顯示該幀的畫面
    cv2.imshow('oxxostudio2', img2)  # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()
