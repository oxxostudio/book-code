# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')

def show_xy(event,x,y,flags,userdata):
    print(event,x,y,flags)
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)  # 設定偵測事件的函式與視窗

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
