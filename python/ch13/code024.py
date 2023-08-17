# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFont, ImageDraw
# import os
img = Image.open('./photo.jpg')
w, h = img.size

font = ImageFont.truetype('Teko-Regular.ttf', 150)
text = Image.new(mode='RGBA', size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), 'OXXO.STUDIO', fill=(255, 255, 255), font=font)
text = text.rotate(30,  expand=1)

img2 = Image.open('./photo.jpg')  # 再次開啟原本的圖為 img2
img2.paste(text, (50, 0), text)   # 將文字貼上 img2
img2.convert('RGBA')              # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img2.putalpha(100)                # 調整透明度，範圍 0～255，0 為全透明
img.paste(img2, (0, 0), img2)     # 將 img2 貼上 img
img.save('./ok.jpg')


