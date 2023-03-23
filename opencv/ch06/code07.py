# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')

x = 135   # 剪裁區域左上 x 座標
y = 90    # 剪裁區域左上 y 座標
cw = 100  # 剪裁區域寬度
ch = 120  # 剪裁區域高度
mosaic = img[y:y+ch, x:x+cw]   # 取得剪裁區域
level = 15         # 馬賽克程度
h = int(ch/level)  # 縮小的高度 ( 使用 int 去除小數點 )
w = int(cw/level)  # 縮小的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_LINEAR)
mosaic = cv2.resize(mosaic, (cw,ch), interpolation=cv2.INTER_NEAREST)
img[y:y+ch, x:x+cw] = mosaic   # 將圖片的剪裁區域，換成馬賽克的圖
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
