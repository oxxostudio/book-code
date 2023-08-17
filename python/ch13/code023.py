# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFont, ImageDraw
img = Image.open('./photo.jpg')
font = ImageFont.truetype('Teko-Regular.ttf', 150)
# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode='RGBA', size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), 'OXXO.STUDIO', fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30,  expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
img.paste(text, (50, 0), text)     # 將文字的圖片貼上原本的圖
img.save('./ok.jpg')


