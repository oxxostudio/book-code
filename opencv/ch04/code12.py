# Copyright © https://steam.oxxostudio.tw

import cv2
img_red = cv2.imread('test-red.png')
img_green = cv2.imread('test-green.png')
img_blue = cv2.imread('test-blue.png')

output = cv2.add(img_red, img_green)  # 疊加紅色和綠色
output = cv2.add(output, img_blue)    # 疊加藍色

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
