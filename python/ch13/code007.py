# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image
imgs = glob.glob('./oxxo/*.jpg')
for i in imgs:
    im = Image.open(i)
    size = im.size
    name = i.split('/')[::-1][0]        # 取得圖片的名稱
    im2 = im.resize((200, 200))         # 調整圖片尺寸為 200x200
    im2.save(f'./oxxo/resize/{name}')   # 調整後存檔到 resize 資料夾

