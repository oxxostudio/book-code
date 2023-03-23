# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg', cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
# img = cv2.imread('meme.jpg', 2) # 也可使用數字代表模式
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
