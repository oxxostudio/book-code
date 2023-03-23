# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
logo = cv2.imread('opencv-logo.jpg')
output = cv2.addWeighted(img, 0.5, logo, 0.3, 50)

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()
