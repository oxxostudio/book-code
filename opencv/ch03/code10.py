# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (width,  height))
# 如果轉換成黑白影片後如果無法開啟，請加上 isColor=False 參數設定
# out = cv2.VideoWriter('output.mov', fourcc, 20.0, (width,  height), isColor=False)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    out.write(gray)
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
