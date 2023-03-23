# Copyright © https://steam.oxxostudio.tw

import cv2
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
output = cv2.bitwise_xor(img1, img2)  # 使用 bitwise_xor
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
