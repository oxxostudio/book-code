# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

def convex(src_img, raw, effect):
    col, row, channel = raw[:]
    cx, cy, r = effect[:]
    output = np.zeros([row, col, channel], dtype = np.uint8)
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5
            if d <= r:
                nx = int((x - cx) * d / r + cx)
                ny = int((y - cy) * d / r + cy)
                output[y, x, :] = src_img[ny, nx, :]
            else:
                output[y, x, :] = src_img[y, x, :]
    return output

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    scale = 0.75
    w, h = int(640*scale), int(320*scale)
    cw, ch = int(w/2), int(h/2)            # 取得中心點
    img = cv2.resize(img,(w, h))           # 調整尺寸，加快速度
    img = convex(img, (w, h, 3), (cw, ch, 100))
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
