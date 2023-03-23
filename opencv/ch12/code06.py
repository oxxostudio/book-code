# Copyright © https://steam.oxxostudio.tw

import cv2
from deepface import DeepFace
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 定義該情緒的中文字
text_obj={
    'angry': '生氣',
    'disgust': '噁心',
    'fear': '害怕',
    'happy': '開心',
    'sad': '難過',
    'surprise': '驚訝',
    'neutral': '正常'
}

# 定義加入文字函式
def putText(x,y,text,size=70,color=(255,255,255)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

img = cv2.imread('emotion.jpg')                    # 載入圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")   # 載入人臉模型
faces = face_cascade.detectMultiScale(gray)        # 偵測人臉

for (x, y, w, h) in faces:
    # 擴大偵測範圍，避免無法辨識情緒
    x1 = x-60
    x2 = x+w+60
    y1 = y-20
    y2 = y+h+60
    face = img[x1:x2, y1:y2]  # 取出人臉範圍
    try:
        emotion = DeepFace.analyze(face, actions=['emotion'])  # 辨識情緒
        putText(x,y,text_obj[emotion['dominant_emotion']])     # 放入文字
    except:
        pass
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
