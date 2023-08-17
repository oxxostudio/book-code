# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('./watermark-photo.jpg')    # 開啟風景圖
icon = Image.open('./oxxostudio-icon.png')   # 開啟浮水印 icon
img.paste(icon, (0,0), icon)     # 將風景圖貼上 icon
img.save('./ok.jpg')             # 存檔為 ok.jpg
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器

