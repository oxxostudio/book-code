# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')

dots = []   # 記錄座標的空串列
def show_xy(event,x,y,flags,param):
    if event == 1:
        dots.append([x, y])                          # 記錄座標
        cv2.circle(img, (x, y), 10, (0,0,255), -1)   # 在點擊的位置，繪製圓形
        num = len(dots)                              # 目前有幾個座標
        if num > 1:                                  # 如果有兩個點以上
            x1 = dots[num-2][0]
            y1 = dots[num-2][1]
            x2 = dots[num-1][0]
            y2 = dots[num-1][1]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)  # 取得最後的兩個座標，繪製直線
        cv2.imshow('oxxostudio', img)

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
