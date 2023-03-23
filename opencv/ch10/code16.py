# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

w = 640    # 定義影片寬度
h = 360    # 定義影像高度
dots = []  # 記錄座標
mask_b = np.zeros((h,w,3), dtype='uint8')   # 產生黑色遮罩 -> 套用清楚影像
mask_b[:, :] = 255                          # 設定黑色遮罩底色為白色
mask_b[80:280, 220:420] = 0                 # 設定黑色遮罩哪個區域是黑色

mask_w = np.zeros((h,w,3), dtype='uint8')   # 產生白色遮罩 -> 套用模糊影像
mask_w[80:280, 220:420] = 255               # 設定白色遮罩哪個區域是白色

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    img = cv2.resize(img,(w,h))                      # 縮小尺寸，加快速度
    img = cv2.flip(img, 1)                           # 翻轉影像
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)      # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
    img2 = img.copy()                                # 複製影像
    img2 = cv2.blur(img, (55, 55))                   # 套用模糊

    mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY) # 轉換遮罩為灰階
    img = cv2.bitwise_and(img, img, mask=mask1)      # 清楚影像套用黑遮罩

    mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY) # 轉換遮罩為灰階
    img2 = cv2.bitwise_and(img2, img2, mask=mask2)   # 模糊影像套用白遮罩

    output = cv2.add(img, img2)                      # 合併影像

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
