# Copyright © https://steam.oxxostudio.tw

import cv2
img1 = cv2.imread('test1.png')
output = cv2.bitwise_not(img1)  # 使用 bitwise_not
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
