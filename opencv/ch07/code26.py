# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread("qrcode.jpg")

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)

# 取得座標的函式
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)   # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin,ymin,xmax,ymax)

# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 畫矩形

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
