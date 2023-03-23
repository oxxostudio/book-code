# Copyright © https://steam.oxxostudio.tw

import cv2
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap1.isOpened():
    print("Cannot open camera1")
    exit()
if not cap2.isOpened():
    print("Cannot open camera2")
    exit()

while True:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    img1 = cv2.resize(img1,(200,150))  # 縮小尺寸
    img2 = cv2.resize(img2,(540,320))  # 縮小尺寸
    img2[160:310,330:530] = img1       # 將 img2 的特定區域換成 img1

    cv2.rectangle(img2, (330,160), (530,310), (255,255,255), 5)  # 繪製子影片的外框

    cv2.imshow('oxxostudio', img2)
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()

