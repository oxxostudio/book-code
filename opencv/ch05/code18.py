# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')
cv2.circle(img,(150,150),100,(0,0,255),-1)  # 設定 -1
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
