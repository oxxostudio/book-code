# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFont, ImageDraw
img = Image.open('./photo.jpg')
w, h = img.size    # 取得圖片尺寸
font = ImageFont.truetype('Teko-Regular.ttf', 100)
draw = ImageDraw.Draw(img)
draw.text((0,h-100), 'OXXO.STUDIO', fill=(255,255,255), font=font)  # 使用 h-100 定位到下方
img.save('./ok.jpg')


