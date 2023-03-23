# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('logo.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h = img.shape[0]
w = img.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            img[y, x] = [0,255,255,255]  # 換成黃色

cv2.imwrite('oxxostudio.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
