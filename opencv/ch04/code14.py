# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('test.png')
img2 = cv2.imread('test2.png')
output = cv2.subtract(img, img2)  # 相減
cv2.imwrite('output.png', output)
cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()
