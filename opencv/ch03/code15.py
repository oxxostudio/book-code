# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme-test.png')
b, g, r = cv2.split(img)
print(b)
print(g)
print(r)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
