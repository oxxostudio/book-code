# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')
cv2.arrowedLine(img,(50,50),(250,250),(0,0,255),5)  # 繪製箭頭線條
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
