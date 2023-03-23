from PIL import Image,ImageSequence
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

gif = Image.open('dot.gif')

img_list = []                                      # 建立儲存影格的空串列
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')                  # 轉換成 RGBA
    opencv_img = np.array(frame, dtype=np.uint8)   # 轉換成 numpy 陣列
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)  # 顏色從 RGBA 轉換為 BGRA
    img_list.append(opencv_img)                    # 利用串列儲存該圖片資訊

loop = True                                        # 設定 loop 為 True
while loop:
    for i in img_list:
        cv2.imshow('oxxostudio', i)                # 不斷讀取並顯示串列中的圖片內容
        if cv2.waitKey(200) == ord('q'):
            loop = False                           # 停止時同時也將 while 迴圈停止
            break
cv2.destroyAllWindows()
