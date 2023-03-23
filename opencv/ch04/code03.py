# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')
rows = img.shape[0]     # 取得高度的總像素
cols = img.shape[1]     # 取得寬度的總像素

for row in range(rows):
    for col in range(cols):
        img[row, col, 0] = 255 - img[row, col, 0]   # 255 - 藍色
        img[row, col, 1] = 255 - img[row, col, 1]   # 255 - 綠色
        img[row, col, 2] = 255 - img[row, col, 2]   # 255 - 紅色

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)          # 按下任意鍵停止
cv2.destroyAllWindows()
