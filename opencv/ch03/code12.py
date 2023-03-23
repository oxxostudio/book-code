# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
print(img.size)            # 518400 ( 360x480x3 )
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
