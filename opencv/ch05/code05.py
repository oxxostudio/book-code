# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
fourcc = cv2.VideoWriter_fourcc(*'MJPG')          # 設定影片的格式為 MJPG
out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (640,  360))  # 產生空的影片，尺寸為 640x360
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img_1 = cv2.resize(frame,(640, 360))   # 改變圖片尺寸
    img_2 = cv2.flip(img_1, 0)             # 上下翻轉
    out.write(img_2)                       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break                              # 按下 q 鍵停止
cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()
