# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(540,320))              # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
    faces = face_cascade.detectMultiScale(gray)      # 偵測人臉
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 標記人臉
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
