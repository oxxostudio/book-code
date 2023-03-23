# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')
pts = np.array([[150,50],[250,100],[150,250],[50,100]])   # 產生座標陣列
cv2.polylines(img,[pts],True,(0,0,255),5)   # 繪製多邊形
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
