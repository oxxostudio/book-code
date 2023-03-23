# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((300,300,3), dtype='uint8')
cv2.ellipse(img,(150,150),(100,50),45,0,360,(0,0,255),5)
cv2.ellipse(img,(150,150),(30,100),90,0,360,(255,150,0),5)
cv2.ellipse(img,(150,150),(20,120),30,0,360,(0,255,255),5)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
