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
def putText(x,y,text,size=50,color=(255,255,255)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text_obj[text], fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(384,240))
    try:
        analyze = DeepFace.analyze(img, actions=['emotion'])
        emotion = analyze['dominant_emotion']  # 取得情緒文字
        putText(0,40,emotion)                  # 放入文字
    except:
        pass
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
