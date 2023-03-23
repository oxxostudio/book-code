# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 640, 360                                   # 定義長寬
a = 1                                             # 存檔的檔名編號從 1 開始
run = 0                                           # 是否開始，0 表示尚未開始，1 表示開始
output = np.zeros((h,h,3), dtype='uint8')         # 設定合成的影像為一張全黑的畫布
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))                   # 縮小尺寸加快速度
    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

    keyCode = cv2.waitKey(10)                     # 等待鍵盤事件
    if keyCode == ord('a') and run == 0:
        y = 0                                     # 如果按下 a，設定 y 為 0
        run = 1                                   # 開始合成
    elif keyCode == ord('q'):
        break                                     # 按下 q 就全部結束

    if run == 1:
        output[y:y+2, 0:h] = img[y:y+2, 0:h]      # 設定 output 的某個區域為即時影像 img 的某區域
        cv2.line(img,(0,y+5),(h,y+5),(0,0,255),5) # 畫線
        y = y + 2                                 # 改變 x 位置
        img[0:y,0:h] = output[0:y,0:h]            # 設定即時影像 img 的某區域為 output
        cv2.imshow('oxxostudio',img)              # 顯示即時影像
        if y > h:
            keyCode = cv2.waitKey() == ord('s')   # 如果寬度抵達正方形邊緣，等待鍵盤事件按下 s
            cv2.imwrite(f'oxxo-{a}.jpg',img)      # 存檔
            a = a + 1                             # 檔名編號增加 1
            run = 0                               # 停止合成
    else:
        cv2.imshow('oxxostudio',img)              # 正常狀況下，一直顯示即時影像

cap.release()
cv2.destroyAllWindows()
