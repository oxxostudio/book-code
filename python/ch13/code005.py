# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image
imgs = glob.glob('./oxxo/*.jpg')     # 取得 demo 資料夾內所有的圖片
for i in imgs:
    im = Image.open(i)    # 依序開啟每一張圖片
    size = im.size        # 取得圖片尺寸
    print(size)

