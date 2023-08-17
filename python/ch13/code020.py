# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('./watermark-photo.jpg')     # 準備合成浮水印的圖
img2 = Image.open('./watermark-photo.jpg')    # 底圖
icon = Image.open('./oxxostudio-icon.png')

img_w, img_h = img.size
icon_w, icon_h = icon.size
x = int((img_w-icon_w)/2)
y = int((img_h-icon_h)/2)
img.paste(icon, (x, y), icon)   # 合成浮水印
img.convert('RGBA')             # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img.putalpha(100)               # 調整透明度，範圍 0～255，0 為全透明
img2.paste(img,(0,0),img)       # 合成底圖
img2.save('./ok.jpg')


