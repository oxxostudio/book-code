# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter
img = Image.open('oxxostudio.jpg')
for i in range(3):
    img = img.filter(ImageFilter.SHARPEN)
img.save('output.jpg')


