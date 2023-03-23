# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp     # 載入 mediapipe 函式庫

cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection   # 建立偵測方法
mp_drawing = mp.solutions.drawing_utils           # 建立繪圖方法

with mp_face_detection.FaceDetection(             # 開始偵測人臉
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 顏色轉換成 RGB
        results = face_detection.process(img2)        # 偵測人臉

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)  # 標記人臉

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
