# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image
jpg = glob.glob('./demo/*.[jJ][pP][gG]')
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)    # 開啟圖片檔案
    name = i.split('/')[::-1][0]         # 取出檔名
    im.save(f'./demo/jpg/{name}', quality=65, subsampling=0)   # 設定參數並存檔

