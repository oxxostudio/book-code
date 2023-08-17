# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('./watermark-photo.jpg')
icon = Image.open('./oxxostudio-icon.png')

img_w, img_h = img.size      # 取得風景圖尺寸
icon_w, icon_h = icon.size   # 取得 icon 尺寸
x = int((img_w-icon_w)/2)    # 計算置中時 icon 左上角的 x 座標
y = int((img_h-icon_h)/2)    # 計算置中時 icon 左上角的 y 座標

img.paste(icon, (x, y), icon)   # 設定 icon 左上角座標
img.save('./ok.jpg')


