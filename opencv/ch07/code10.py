# Copyright © https://steam.oxxostudio.tw

import cv2
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
mask = cv2.imread('mask.png')                    # 遮罩圖片
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)    # 轉換成灰階模式
output = cv2.bitwise_xor(img1, img2, mask=mask)  # 加入 mask 參數
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
