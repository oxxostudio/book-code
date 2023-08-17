# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('oxxostudio.jpg')                  # 開啟圖片
w,h = img.size                                      # 讀取圖片長寬
level = 50                                          # 設定縮小程度
img2 = img.resize((int(w/level),int(h/level)))      # 縮小圖片
img2 = img2.resize((w,h), resample = Image.NEAREST) # 放大圖片為原始大小
img2.save('test.jpg')                               # 存檔


