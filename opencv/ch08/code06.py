# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('oxxostudio', img2)
        if event == 4:
            level = 8                                         # 縮小比例 ( 可當作馬賽克的等級 )
            h = int((dot2[0] - dot1[0]) / level)              # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
            w = int((dot2[1] - dot1[1]) / level)              # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
            mosaic = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]    # 取得馬賽克區域
            mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
            mosaic = cv2.resize(mosaic, (dot2[0] - dot1[0], dot2[1] - dot1[1]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
            img[dot1[1]:dot2[1], dot1[0]:dot2[0]] = mosaic   # 置換成馬賽克的影像
            cv2.imshow('oxxostudio', img)

cv2.imshow('oxxostudio', img)
cv2.setMouseCallback('oxxostudio', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
