import tensorflow as tf
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 50)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text('剪刀')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('石頭')
    if c>0.9:
        text('布')
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
