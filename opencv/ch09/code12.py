# Copyright © https://steam.oxxostudio.tw

import cv2

tracker = cv2.TrackerCSRT_create()  # 創建追蹤器
tracking = False                    # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(540,300))  # 縮小尺寸，加快速度
    keyName = cv2.waitKey(1)

    if keyName == ord('q'):
        break
    if keyName == ord('a'):
        area = cv2.selectROI('oxxostudio', frame, showCrosshair=False, fromCenter=False)
        tracker.init(frame, area)    # 初始化追蹤器
        tracking = True              # 設定可以開始追蹤
    if tracking:
        success, point = tracker.update(frame)   # 追蹤成功後，不斷回傳左上和右下的座標
        if success:
            p1 = [int(point[0]), int(point[1])]
            p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
            cv2.rectangle(frame, p1, p2, (0,0,255), 3)   # 根據座標，繪製四邊形，框住要追蹤的物件

    cv2.imshow('oxxostudio', frame)

cap.release()
cv2.destroyAllWindows()
