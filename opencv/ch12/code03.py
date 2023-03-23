# Copyright © https://steam.oxxostudio.tw

import cv2
from deepface import DeepFace
import numpy as np

img = cv2.imread('test.jpg')     # 讀取圖片
try:
    analyze = DeepFace.analyze(img)  # 辨識圖片人臉資訊
    print(analyze)
except:
    pass

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
