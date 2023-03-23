# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_objectron = mp.solutions.objectron    # mediapipe 物體偵測

cap = cv2.VideoCapture(0)

# 啟用物體偵測，偵測鞋子 Shoe
with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.99,
                            model_name='Shoe') as objectron:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))               # 縮小尺寸，加快演算速度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = objectron.process(img2)             # 取得物體偵測結果
        # 標記所偵測到的物體
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                  img, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(img, detected_object.rotation,
                                    detected_object.translation)

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
