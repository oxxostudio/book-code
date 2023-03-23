# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')
rows = img.shape[0]
cols = img.shape[1]

for row in range(int(rows/2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        img[row, col, 0] = 255 - img[row, col, 0]
        img[row, col, 1] = 255 - img[row, col, 1]
        img[row, col, 2] = 255 - img[row, col, 2]

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
