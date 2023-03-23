# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

def convex(src_img, raw, effect):
    col, row, channel = raw[:]      # 取得圖片資訊
    cx, cy, r = effect[:]           # 取得凸透鏡的範圍
    output = np.zeros([row, col, channel], dtype = np.uint8)        # 產生空白畫布
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5  # 計算每個點與中心點的距離
            if d <= r:
                nx = int((x - cx) * d / r + cx)        # 根據不同的位置，產生新的 nx，越靠近中心形變越大
                ny = int((y - cy) * d / r + cy)        # 根據不同的位置，產生新的 ny，越靠近中心形變越大
                output[y, x, :] = src_img[ny, nx, :]   # 產生新的圖
            else:
                output[y, x, :] = src_img[y, x, :]     # 如果在半徑範圍之外，原封不動複製過去
    return output

img = cv2.imread('mona.jpg')
img = convex(img, (300, 400, 3), (150, 130, 100))      # 提交參數數值，進行凸透鏡效果
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
