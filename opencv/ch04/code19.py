# Copyright © https://steam.oxxostudio.tw

import cv2
img1 = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
print(img1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(img2.shape)    # (400, 300, 4)  PNG 四個色版 GRA
