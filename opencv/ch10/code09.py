# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
bg = cv2.imread('windows-bg.jpg')   # 載入 windows 經典背景

with mp_pose.Pose(
    min_detection_confidence=0.5,
    enable_segmentation=True,       # 額外設定 enable_segmentation 參數
    min_tracking_confidence=0.5) as pose:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img2)
        try:
            # 使用 try 避免抓不到姿勢時發生錯誤
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
            # 如果滿足模型判斷條件 ( 表示要換成背景 )，回傳 True
            img = np.where(condition, img, bg)
            # 將主體與背景合成，如果滿足背景條件，就更換為 bg 的像素，不然維持原本的 img 的像素
        except:
            pass
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
