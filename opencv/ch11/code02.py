import tensorflow as tf
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 2.5                      # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 5                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

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
        text('a')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('b')
    if c>0.9:
        text('c')
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
