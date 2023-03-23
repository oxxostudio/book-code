# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')
img[50:250, 50:250] = [0,0,255] # 將中間 200x200 的陣列內容改成 [0,0,255]
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
