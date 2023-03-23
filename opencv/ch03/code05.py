# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((500,500,3), dtype='uint8')   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]
cv2.imwrite('oxxostudio.jpg', img)       # 存成 jpg
cv2.imshow('oxxostudio', img)            # 顯示圖片
cv2.waitKey(0)                           # 按下任意鍵停止
cv2.destroyAllWindows()
