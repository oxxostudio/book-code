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
    name = i.lower().split('/')[::-1][0]         # 將檔名換成小寫 ( 避免 JPG 與 jpg 干擾 )
    png = name.replace('jpg','png')  # 取出圖片檔名，將 jpg 換成 png
    im.save(f'./demo/png/{png}', 'png')   # 轉換成 png 並存檔

