import tensorflow as tf
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

model = tf.keras.models.load_model('keras_model.h5', compile=False)   # 載入 model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)           # 設定資料陣列

cap = cv2.VideoCapture(0)         # 設定攝影機鏡頭
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()       # 讀取攝影機影像
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))   # 改變尺寸
    img = img[0:224, 80:304]               # 裁切為正方形，符合 model 大小
    image_array = np.asarray(img)          # 去除換行符號和結尾空白，產生文字陣列
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # 轉換成預測陣列
    data[0] = normalized_image_array
    prediction = model.predict(data)       # 預測結果
    a,b= prediction[0]                     # 取得預測結果
    if a>0.9:
        print('oxxo')
    if b>0.9:
        print('維他命')
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(500) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
