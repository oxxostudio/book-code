# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter
img = Image.open('oxxostudio.jpg')
output = img.filter(ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10))    # 套用 UnsharpMask
output.show()


