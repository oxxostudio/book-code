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
    keyName = cv2.waitKey(1)
    # 按下 q 結束
    if keyName == ord('q'):
        break
    # 按下 a 開始選取
    if keyName == ord('a'):
        # 選取區域
        area = cv2.selectROI('oxxostudio', frame, showCrosshair=False, fromCenter=False)
        print(area)

    cv2.imshow('oxxostudio', frame)

cap.release()
cv2.destroyAllWindows()
