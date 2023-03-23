# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
cv2.imwrite('oxxo', img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()
