# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageEnhance
img = Image.open("oxxostudio.png")         # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(factor)        # 調整亮度，factor 為一個浮點數值
                                           # 調整後的數值 = 原始數值 x factor

