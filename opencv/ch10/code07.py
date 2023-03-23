# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp
import random

mp_drawing = mp.solutions.drawing_utils          # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_hands = mp.solutions.hands                    # mediapipe 偵測手掌方法

cap = cv2.VideoCapture(0)

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    run = True         # 設定是否更動觸碰區位置
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(540,320))  # 調整畫面尺寸
        size = img.shape   # 取得攝影機影像尺寸
        w = size[1]        # 取得畫面寬度
        h = size[0]        # 取得畫面高度
        if run:
            run = False    # 如果沒有碰到，就一直是 False ( 不會更換位置 )
            rx = random.randint(50,w-50)    # 隨機 x 座標
            ry = random.randint(50,h-100)   # 隨機 y 座標
            print(rx, ry)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = hands.process(img2)                 # 偵測手掌
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x = hand_landmarks.landmark[7].x * w   # 取得食指末端 x 座標
                y = hand_landmarks.landmark[7].y * h   # 取得食指末端 y 座標
                print(x,y)
                if x>rx and x<(rx+80) and y>ry and y<(ry+80):
                    run = True
                # 將節點和骨架繪製到影像中
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        cv2.rectangle(img,(rx,ry),(rx+80,ry+80),(0,0,255),5)   # 畫出觸碰區
        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
