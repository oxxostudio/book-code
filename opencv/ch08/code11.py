# Copyright © https://steam.oxxostudio.tw

import cv2

img = cv2.imread('mona.jpg')
cv2.imshow('oxxostudio', img)

def test(val):
    print(val)

cv2.createTrackbar('test', 'oxxostudio', 0, 255, test)
cv2.setTrackbarPos('test', 'oxxostudio', 50)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()
