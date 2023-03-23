# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

w = 400
h = 400
img = np.zeros([h,w,3])
for i in range(h):
    for j in range(w):
        img[i,j,0] = int(256*(j+i)/(w+h))
        img[i,j,2] = int(256*(j+i)/(w+h))

img = img.astype('float32')/255

cv2.imshow('oxxostudio', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
