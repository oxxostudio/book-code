# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image
imgs = glob.glob('./demo/*.jpg')     # 讀取 demo 資料夾裡所有的圖片
icon = Image.open('./oxxostudio-icon.png')
for i in imgs:
    name = i.split('/')[::-1][0]   # 取得圖片名稱
    img = Image.open(i)            # 開啟圖片
    img.paste(icon, (0,0), icon)   # 加入浮水印
    img.save(f'./demo/watermark/{name}')   # 以原本的名稱存檔


