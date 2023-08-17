# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif
img = Image.open("./oxxostudio.jpg")       # 使用 PIL Image 開啟圖片
exif = piexif.load(img.info["exif"])   # 使用 piexif 讀取圖片 Exif 資訊
print(exif)


