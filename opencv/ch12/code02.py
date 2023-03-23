# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)                     # 啟用攝影鏡頭
print('loading...')
knn = cv2.ml.KNearest_load('mnist_knn.xml')   # 載入模型
print('start...')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(540,300))          # 改變影像尺寸，加快處理效率
    x, y, w, h = 400, 200, 60, 60            # 定義擷取數字的區域位置和大小
    img_num = img.copy()                     # 複製一個影像作為辨識使用
    img_num = img_num[y:y+h, x:x+w]          # 擷取辨識的區域

    img_num = cv2.cvtColor(img_num, cv2.COLOR_BGR2GRAY)    # 顏色轉成灰階
    # 針對白色文字，做二值化黑白轉換，轉成黑底白字
    ret, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
    output = cv2.cvtColor(img_num, cv2.COLOR_GRAY2BGR)     # 顏色轉成彩色
    img[0:60, 480:540] = output                            # 將轉換後的影像顯示在畫面右上角

    img_num = cv2.resize(img_num,(28,28))   # 縮小成 28x28，和訓練模型對照
    img_num = img_num.astype(np.float32)    # 轉換格式
    img_num = img_num.reshape(-1,)          # 打散成一維陣列資料，轉換成辨識使用的格式
    img_num = img_num.reshape(1,-1)
    img_num = img_num/255
    img_pre = knn.predict(img_num)          # 進行辨識
    num = str(int(img_pre[1][0][0]))        # 取得辨識結果

    text = num                              # 印出的文字內容
    org = (x,y-20)                          # 印出的文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX     # 印出的文字字體
    fontScale = 2                           # 印出的文字大小
    color = (0,0,255)                       # 印出的文字顏色
    thickness = 2                           # 印出的文字邊框粗細
    lineType = cv2.LINE_AA                  # 印出的文字邊框樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 印出文字

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)  # 標記辨識的區域
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(50) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
