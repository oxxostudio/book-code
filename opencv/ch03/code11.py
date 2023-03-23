# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
print(img.shape)            # 得到 (360, 480, 3)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)              # 按下任意鍵停止
cv2.destroyAllWindows()
