# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')

def show_xy(event,x,y,flags,param):
    if event == 0:
        img2 = img.copy()                         # 當滑鼠移動時，複製原本的圖片
        cv2.circle(img2, (x,y), 10, (0,0,0), 1)   # 繪製黑色空心圓
        cv2.imshow('oxxostudio', img2)            # 顯示繪製後的影像
    if event == 1:
        color = img[y,x]                          # 當滑鼠點擊時
        print(color)                              # 印出顏色

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
