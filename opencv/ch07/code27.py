# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image          # 載入 PIL ( 為了放中文字 )
img = cv2.imread("qrcode.jpg")

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)

# 建立放入文字的函式
def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(fontpath, 20)  # 設定字型與大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 圖片物件
    draw = ImageDraw.Draw(imgPil)            # 建立繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 寫入文字
    img = np.array(imgPil)                   # 轉換回 np array

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
