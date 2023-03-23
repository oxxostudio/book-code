# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread('meme.jpg')
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]

output = np.zeros((360,480,3), dtype='uint8') # 產生黑色畫布
output[x:x+w, y:y+h]=crop_img

cv2.imwrite('output.jpg', output)
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
