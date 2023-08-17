# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from PIL import Image, ImageFont, ImageDraw

img = Image.new('RGBA', (360, 180))                       # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片
font = ImageFont.truetype('NotoSansTC-Regular.otf', 40)   # 設定字型與尺寸
draw = ImageDraw.Draw(img)                                # 準備在圖片上繪圖
# 將文字畫入圖片
draw.text((10,120),'OXXO.STUDIO',fill=(255,255,255),font=font,stroke_width=2,stroke_fill='red')
draw.text(xy=(50,0), text='大家好\n哈哈', align='center', fill=(255,255,255), font=font, stroke_width=2, stroke_fill='blue')
img.save('ok.png')    # 儲存為 png

