# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread("qrcode.jpg")                       # 開啟圖片

qrcode = cv2.QRCodeDetector()                        # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(img)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)                # QRCode 的內容
    print(bbox)                # QRCode 的邊界
    print(rectified)           # 換成垂直 90 度的陣列

cv2.imshow('oxxostudio', img)  # 預覽圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗
