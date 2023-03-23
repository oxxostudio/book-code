# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
img = np.zeros((150,300,3), dtype='uint8')   # 建立 300x150 的黑色畫布
text = 'Hello'
org = (20,90)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0,0,255)
thickness = 5
lineType = cv2.LINE_AA
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()
