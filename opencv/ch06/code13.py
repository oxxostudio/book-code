# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
output = np.zeros((360,640,3), dtype='uint8')

if not cap.isOpened():
    print("Cannot open camera")
    exit()

n = 5
w = 640//n
h = 360//n
img_list = []        # 設定空串列，記錄每一格的影像
while True:
    ret, img = cap.read()
    img = cv2.resize(img,(w, h))
    img_list.append(img)                    # 每次擷取影像時，將影像存入串列
    if len(img_list)>n*n: del img_list[0]   # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i%n      # 根據串列計算影像的 x 座標 ( 取餘數 )
        y = i//n     # 根據串列計算影像的 y 座標 ( 取整數 )
        output[h*y:h*y+h, w*x:w*x+w] = img_list[i]  # 更新畫面

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
