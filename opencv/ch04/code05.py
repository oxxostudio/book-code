# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('mona.jpg')

img = 255-img # 使用 255 減去陣列中所有數值

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
