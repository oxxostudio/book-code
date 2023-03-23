# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
