# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)            # 讀取攝影機

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    w = 640    # 定義影片寬度
    h = 360    # 定義影像高度
    dots = []  # 記錄座標
    mask_b = np.zeros((h,w,3), dtype='uint8')            # 產生黑色遮罩 -> 套用清楚影像
    mask_w = np.zeros((h,w,3), dtype='uint8')            # 產生白色遮罩 -> 套用模糊影像
    mask_w[0:h, 0:w] = 255                               # 白色遮罩背景為白色

    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w,h))                     # 縮小尺寸，加快處理效率
        img = cv2.flip(img, 1)                           # 翻轉影像
        img_hand = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 偵測手勢使用
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)      # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
        img2 = img.copy()                                # 複製影像
        img2 = cv2.blur(img, (55, 55))                   # 套用模糊

        if not ret:
            print("Cannot receive frame")
            break
        results = hands.process(img_hand)                # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []                       # 記錄手指節點位置的串列
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    finger_points.append((x,y))          # 記錄手指節點位置
                if finger_points:
                    fx1 = finger_points[8][0]
                    fy1 = finger_points[8][1]
                    fx2 = finger_points[12][0]
                    fy2 = finger_points[12][1]
                    d = ((fx1-fx2)*(fx1-fx2)+(fy1-fy2)*(fy1-fy2))**0.5  # 計算食指和中指分開的距離
                    if d<0.15:
                        dots.append([fx1,fy1])
                        dl = len(dots)
                        if dl>1:
                            x1 = int(dots[dl-2][0]*w)   # 計算出真正的座標
                            y1 = int(dots[dl-2][1]*h)
                            x2 = int(dots[dl-1][0]*w)
                            y2 = int(dots[dl-1][1]*h)
                            cv2.line(mask_w, (x1,y1), (x2,y2), (0,0,0), 50)        # 在白色遮罩上畫出黑色線條
                            cv2.line(mask_b, (x1,y1), (x2,y2), (255,255,255), 50)  # 在黑色遮罩上畫出白色線條
                    else:
                        dots = []

        mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY) # 轉換遮罩為灰階
        img = cv2.bitwise_and(img, img, mask=mask1)      # 清楚影像套用黑遮罩
        mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY) # 轉換遮罩為灰階
        img2 = cv2.bitwise_and(img2, img2, mask=mask2)   # 模糊影像套用白遮罩

        output = cv2.add(img, img2)                      # 合併影像

        cv2.imshow('oxxostudio', output)
        keyboard = cv2.waitKey(5)
        if keyboard == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
