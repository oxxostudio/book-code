# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

mask = np.zeros((300,300,3), dtype='uint8')
cv2.circle(mask,(150,150),100,(255,255,255),-1)
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255                          # 除以 255，計算每個像素的黑白色彩在 255 中所佔的比例

img = cv2.imread('mona.jpg')               # 開啟圖片
bg = np.zeros((300,300,3), dtype='uint8')  # 產生一張黑色背景
bg = 255 - bg                              # 轉換成白色背景
img = img / 255                            # 除以 255，計算每個像素的色彩在 255 中所佔的比例
bg = bg / 255                              # 除以 255，計算每個像素的色彩在 255 中所佔的比例

out  = bg * (1 - mask) + img * mask        # 根據比例混合
out = (out * 255).astype('uint8')          # 乘以 255 之後轉換成整數

cv2.imshow('oxxostudio',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
