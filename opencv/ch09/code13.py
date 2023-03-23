# Copyright © https://steam.oxxostudio.tw

import cv2

tracker_list = []
for i in range(3):
    tracker = cv2.TrackerCSRT_create()        # 創建三組追蹤器
    tracker_list.append(tracker)
colors = [(0,0,255),(0,255,255),(255,255,0)]  # 設定三個外框顏色
tracking = False                              # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture('test.mov')            # 讀取某個影片
a = 0                                         # 刪減影片影格使用
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(400,230))       # 縮小尺寸，加快速度
    keyName = cv2.waitKey(1)
    # 為了避免影片影格太多，所以採用 10 格取一格，加快處理速度
    if a%10 == 0:
        if keyName == ord('q'):
            break
        if tracking == False:
            # 如果尚未開始追蹤，就開始標記追蹤物件的外框
            for i in tracker_list:
                area = cv2.selectROI('oxxostudio', frame, showCrosshair=False, fromCenter=False)
                i.init(frame, area)    # 初始化追蹤器
            tracking = True            # 設定可以開始追蹤
        if tracking:
            for i in range(len(tracker_list)):
                success, point = tracker_list[i].update(frame)   # 追蹤成功後，不斷回傳左上和右下的座標
                if success:
                    p1 = [int(point[0]), int(point[1])]
                    p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
                    cv2.rectangle(frame, p1, p2, colors[i], 3)   # 根據座標，繪製四邊形，框住要追蹤的物件

        cv2.imshow('oxxostudio', frame)
    a = a + 1

cap.release()
cv2.destroyAllWindows()
