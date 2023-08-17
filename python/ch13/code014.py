# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
bg = Image.new('RGB',(400, 300), '#ff000055')    # 產生 RGBA 色域，400x300 背景半透明紅色的圖片
bg.save('oxxostudio.png')

