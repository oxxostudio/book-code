# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imshow('oxxostudio', img)  # 使用名為 oxxostudio 的視窗開啟圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗
