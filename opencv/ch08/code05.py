# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2    # 因為要讓 img = img2，所以也要宣告 img2 為全域變數
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('oxxostudio', img2)
        if event == 4:
            img = img2   # 滑鼠放開時 ( event == 4 )，將 img 更新為 img2

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
