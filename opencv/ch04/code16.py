# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

w, h = 400, 400
img1 = np.zeros([h,w,3])
for i in range(h):
    img[i,:,1] = int(256*i/400)   # 從上往下填入綠色漸層

img = img.astype('float32')/255   # 轉換內容類型

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)                    # 按下任意鍵停止
cv2.destroyAllWindows()
