# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
lower = np.array([30,40,200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255]) # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
img = cv2.imread('oxxo.jpg')
mask = cv2.inRange(img, lower, upper)             # 使用 inRange
output = cv2.bitwise_and(img, img, mask = mask )  # 套用影像遮罩
cv2.imwrite('output.jpg', output)
cv2.waitKey(0)                                    # 按下任意鍵停止
cv2.destroyAllWindows()
