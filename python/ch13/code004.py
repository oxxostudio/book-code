# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('oxxostudio.jpg')  # 開啟圖片
print(img.size)                     # (1280,720) 印出長寬尺寸
