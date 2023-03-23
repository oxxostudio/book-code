# Copyright © https://steam.oxxostudio.tw

import cv2
img_blue = cv2.imread('meme.jpg')
img_green = cv2.imread('meme.jpg')
img_red = cv2.imread('meme.jpg')
img_blue[:,:,1] = 0    # 將綠色設為 0
img_blue[:,:,2] = 0    # 將紅色設為 0
img_green[:,:,0] = 0   # 將藍色設為 0
img_green[:,:,2] = 0   # 將紅色設為 0
img_red[:,:,0] = 0     # 將藍色設為 0
img_red[:,:,1] = 0     # 將綠色設為 0
cv2.imshow('oxxostudio blue', img_blue)
cv2.imshow('oxxostudio green', img_green)
cv2.imshow('oxxostudio red', img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
