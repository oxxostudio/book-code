# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')
size = img.shape         # 取得原始圖片的資訊
level = 15               # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
cv2.imshow('oxxostudio', mosaic)
cv2.waitKey(0)           # 按下任意鍵停止
cv2.destroyAllWindows()
