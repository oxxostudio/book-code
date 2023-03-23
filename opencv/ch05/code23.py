# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image    # 載入 PIL 相關函式庫
img = np.zeros((150,300,3), dtype='uint8')   # 繪製黑色畫布
fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑
font = ImageFont.truetype(fontpath, 50)      # 設定字型與文字大小
imgPil = Image.fromarray(img)                # 將 img 轉換成 PIL 影像
draw = ImageDraw.Draw(imgPil)                # 準備開始畫畫
draw.text((0, 0), '大家好～\n嘿嘿嘿～', fill=(255, 255, 255), font=font)  # 畫入文字，\n 表示換行
img = np.array(imgPil)                       # 將 PIL 影像轉換成 numpy 陣列
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
