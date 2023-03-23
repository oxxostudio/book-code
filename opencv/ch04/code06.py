# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = cv2.imread('mona.jpg')

contrast = 200
brightness = 0
output = img * (contrast/127 + 1) - contrast + brightness # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

cv2.imshow('oxxostudio1', img)    # 原始圖片
cv2.imshow('oxxostudio2', output) # 調整亮度對比的圖片
cv2.waitKey(0)                    # 按下任意鍵停止
cv2.destroyAllWindows()
