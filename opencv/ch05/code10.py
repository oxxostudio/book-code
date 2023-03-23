# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]        # 取出陣列的範圍
cv2.imwrite('output.jpg', crop_img) # 儲存圖片
cv2.imshow('oxxostudio', crop_img)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()
