# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

logo = cv2.imread('logo.jpg')                    # 讀取 OpenCV 的 logo
size = logo.shape                                # 讀取 logo 的長寬尺寸

img = np.zeros((360,480,3), dtype='uint8')       # 產生一張 480x360 背景全黑的圖
img[0:360, 0:480] = '255'                        # 將圖片變成白色 ( 配合 logo 是白色底 )
img[0:size[0], 0:size[1]] = logo                 # 將圖片的指定區域，換成 logo 的圖案
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 產生一張灰階的圖片作為遮罩使用
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)  # 使用二值化的方法，產生黑白遮罩圖片
logo = cv2.bitwise_and(img, img, mask = mask1 )  # logo 套用遮罩

bg = cv2.imread('meme.jpg')                      # 讀取底圖
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)      # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask = mask2 )      # 底圖套用遮罩

output = cv2.add(bg, logo)                       # 使用 add 方法將底圖和 logo 合併
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
