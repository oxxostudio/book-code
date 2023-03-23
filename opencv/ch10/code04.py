# Copyright © https://steam.oxxostudio.tw

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils             # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles     # mediapipe 繪圖樣式
mp_face_mesh = mp.solutions.face_mesh               # mediapipe 人臉網格方法
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)  # 繪圖參數設定

cap = cv2.VideoCapture(0)

# 啟用人臉網格偵測，設定相關參數
with mp_face_mesh.FaceMesh(
    max_num_faces=1,       # 一次偵測最多幾個人臉
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 顏色 BGR 轉換為 RGB
        results = face_mesh.process(img2)             # 取得人臉網格資訊
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 繪製網格
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                # 繪製輪廓
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                # 繪製眼睛
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
