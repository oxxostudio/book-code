# Copyright © https://steam.oxxostudio.tw

import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 640, 360                                   # 定義長寬
x = 0                                             # 定義 x 從 0 開始
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))                   # 縮小尺寸加快速度
    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形
    cv2.line(img,(x,0),(x,h),(0,0,255),5)         # 畫線
    cv2.imshow('oxxostudio',img)                  # 正常狀況下，一直顯示即時影像
    x = x + 2
    if x > h:
        x = 0
    keyCode = cv2.waitKey(10)                     # 等待鍵盤事件
    if keyCode == ord('q'):
        break                                     # 按下 q 就全部結束

cap.release()
cv2.destroyAllWindows()
