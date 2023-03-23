# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_

# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
        )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
        ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
        )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
        ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
        )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
        ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
        )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
        ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
        )
    angle_list.append(angle_)
    return angle_list

# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1'
    else:
        return ''

cap = cv2.VideoCapture(0)            # 讀取攝影機
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA               # 印出文字的邊框

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    w, h = 540, 310                                        # 影像尺寸
    draw = np.zeros((h,w,4), dtype='uint8')                # 繪製全黑背景，尺寸和影像相同
    dots = []                                              # 使用 dots 空串列記錄繪圖座標點
    cv2.rectangle(draw,(20,20),(60,60),(0,0,255,255),-1)   # 在畫面上方放入紅色正方形
    cv2.rectangle(draw,(80,20),(120,60),(0,255,0,255),-1)  # 在畫面上方放入綠色正方形
    cv2.rectangle(draw,(140,20),(180,60),(255,0,0,255),-1) # 在畫面上方放入藍色正方形
    color = (0,0,255,255)                                  # 設定預設顏色為紅色
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w,h))                       # 縮小尺寸，加快處理效率
        img = cv2.flip(img, 1)
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        # 偵測手勢的影像轉換成 RGB 色彩
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)        # 畫圖的影像轉換成 BGRA 色彩
        results = hands.process(img2)                      # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []                         # 記錄手指節點座標的串列
                for i in hand_landmarks.landmark:
                    # 將 21 個節點換算成座標，記錄到 finger_points
                    x = i.x*w
                    y = i.y*h
                    finger_points.append((x,y))
                if finger_points:
                    finger_angle = hand_angle(finger_points) # 計算手指角度，回傳長度為 5 的串列
                    text = hand_pos(finger_angle)            # 取得手勢所回傳的內容
                    if text == '1':
                        fx = int(finger_points[8][0])        # 如果手勢為 1，記錄食指末端的座標
                        fy = int(finger_points[8][1])
                        if fy>=20 and fy<=60 and fx>=20 and fx<=60:
                            color = (0,0,255,255)            # 如果食指末端碰到紅色，顏色改成紅色
                        elif fy>=20 and fy<=60 and fx>=80 and fx<=120:
                            color = (0,255,0,255)            # 如果食指末端碰到綠色，顏色改成綠色
                        elif fy>=20 and fy<=60 and fx>=140 and fx<=180:
                            color = (255,0,0,255)            # 如果食指末端碰到藍色，顏色改成藍色
                        else:
                            dots.append([fx,fy])             # 記錄食指座標
                            dl = len(dots)
                            if dl>1:
                                dx1 = dots[dl-2][0]
                                dy1 = dots[dl-2][1]
                                dx2 = dots[dl-1][0]
                                dy2 = dots[dl-1][1]
                                cv2.line(draw,(dx1,dy1),(dx2,dy2),color,5)  # 在黑色畫布上畫圖
                    else:
                        dots = [] # 如果換成別的手勢，清空 dots

        # 將影像和黑色畫布合成
        for j in range(w):
            img[:,j,0] = img[:,j,0]*(1-draw[:,j,3]/255) + draw[:,j,0]*(draw[:,j,3]/255)
            img[:,j,1] = img[:,j,1]*(1-draw[:,j,3]/255) + draw[:,j,1]*(draw[:,j,3]/255)
            img[:,j,2] = img[:,j,2]*(1-draw[:,j,3]/255) + draw[:,j,2]*(draw[:,j,3]/255)

        cv2.imshow('oxxostudio', img)
        keyboard = cv2.waitKey(5)
        if keyboard == ord('q'):
            break
        # 按下 r 重置畫面
        if keyboard == ord('r'):
            draw = np.zeros((h,w,4), dtype='uint8')
            cv2.rectangle(draw,(20,20),(60,60),(0,0,255,255),-1)   # 在畫面上方放入紅色正方形
            cv2.rectangle(draw,(80,20),(120,60),(0,255,0,255),-1)  # 在畫面上方放入綠色正方形
            cv2.rectangle(draw,(140,20),(180,60),(255,0,0,255),-1) # 在畫面上方放入藍色正方形
cap.release()
cv2.destroyAllWindows()
