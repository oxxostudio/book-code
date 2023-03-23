# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(480,300))              # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 影像轉轉灰階
    faces = face_cascade.detectMultiScale(gray)      # 偵測人臉
    for (x, y, w, h) in faces:
        mosaic = frame[y:y+h, x:x+w]
        level = 15
        mh = int(h/level)
        mw = int(w/level)
        mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR)
        mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = mosaic
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
