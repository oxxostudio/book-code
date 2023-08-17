# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('./oxxostudio.jpg')
img_r1 = img.rotate(30)             # 旋轉 30 度
img_r2 = img.rotate(30,expand=1)    # 旋轉 30 度，expand 設定 1
img_r1.save('./test1.jpg')
img_r2.save('./test2.jpg')
