# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

a = 0    # 白色圖片透明度
n = 0    # 檔名編號

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA
    w = int(img.shape[1]*0.5)           # 縮小寬度為一半
    h = int(img.shape[0]*0.5)           # 縮小高度為一半
    img = cv2.resize(img,(w,h))         # 縮放尺寸
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    key = cv2.waitKey(1)
    if key == 32:            # 按下空白將 a 等於 1
        a = 1
    elif key == ord('q'):    # 按下 q 結束
        break

    if a == 0:
        output = img.copy()  # 如果 a 為 0，設定 output 變數為來源圖片的拷貝
    else:
        photo = img.copy()   # 如果 a 不為 0，設定 photo 變數為來源圖片的拷貝
        output = cv2.addWeighted(white, a, photo, 1-a, 0)  # 計算權重，產生白色慢慢消失效果
        a = a - 0.1
        if a<0:
            a = 0
            n = n + 1
            cv2.imwrite(f'photo-{n}.jpg', photo)   # 存檔

    cv2.imshow('oxxostudio', output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗
