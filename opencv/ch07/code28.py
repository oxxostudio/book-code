# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
img = cv2.imread("many-qrcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(fontpath, 20)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

qrcode = cv2.QRCodeDetector()
ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)   # 改用 detectAndDecodeMulti
# 如果有偵測到
if ok:
    # 使用 for 迴圈取出每個 QRCode 的資訊
    for i in range(len(data)):
        print(data[i])
        print(bbox[i])
        text = data[i]          # QRCode 內容
        box = boxSize(bbox[i])  # QRCode 左上與右下座標
        cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 標記外框
        putText(box[0],box[3],text)   # 寫出文字

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
