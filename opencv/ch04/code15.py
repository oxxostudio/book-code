# Copyright © https://steam.oxxostudio.tw

import cv2
cap = cv2.VideoCapture(0)
logo = cv2.imread('opencv-logo.jpg')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img_1 = cv2.resize(frame,(480, 360))    # 改變影像尺寸，符合疊加的圖片
    output = cv2.addWeighted(img_1, 0.5, logo, 0.3, 50)  # 疊加圖片
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
