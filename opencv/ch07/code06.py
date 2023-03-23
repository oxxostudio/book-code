# Copyright © https://steam.oxxostudio.tw

import cv2
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
output = cv2.bitwise_and(img1, img2)  # 使用 bitwise_and
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()
