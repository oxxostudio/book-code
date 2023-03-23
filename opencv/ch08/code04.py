# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')

dot1 = []                          # 記錄第一個座標
dot2 = []                          # 記錄第二個座標

# 滑鼠事件發生時要執行的函式
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img         # 在函式內使用全域變數
    # 滑鼠拖曳發生時
    if flags == 1:
        if event == 1:
            dot1 = [x, y]          # 按下滑鼠時記錄第一個座標
        if event == 0:
            img2 = img.copy()      # 拖曳時不斷複製 img
            dot2 = [x, y]          # 拖曳時不斷更新第二個座標
            # 根據兩個座標繪製四邊形
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            # 不斷顯示新圖片 ( 如果不這麼做，會出現一堆四邊形殘影 )
            cv2.imshow('oxxostudio', img2)

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)

cv2.waitKey(0)   # 按下任意鍵結束
cv2.destroyAllWindows()
