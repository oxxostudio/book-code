# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

w = 400
h = 400
img = np.zeros([h,w,4])             # 第三個值為 4
for i in range(h):
    img[i,:,3] = int(256*i/400)     # 設定第四個值 ( 透明度 )

img = img.astype('float32')/255

cv2.imwrite('oxxostudio.png', img)  # 儲存為 png

cv2.waitKey(0)
cv2.destroyAllWindows()
