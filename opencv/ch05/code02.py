# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output = cv2.transpose(img)    # 逆時針旋轉 90 度。
cv2.imwrite('output.jpg', output)
