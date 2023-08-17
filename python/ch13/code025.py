# Copyright © https://steam.oxxostudio.tw

from PIL import Image, ImageFont, ImageDraw
# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除
imgs = glob.glob('./demo/*.jpg')     # 讀取 demo 資料夾裡所有的圖片

for i in imgs:
    name = i.split('/')[::-1][0]    # 取得圖片名稱
    img = Image.open(i)             # 開啟圖片
    w, h = img.size
    font = ImageFont.truetype('Teko-Regular.ttf', 100)
    text = Image.new(mode='RGBA', size=(400, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(text)
    draw.text((0, 0), 'OXXO.STUDIO', fill=(255, 255, 255), font=font)
    text = text.rotate(30,  expand=1)
    img2 = Image.open(i)
    img2.paste(text, (50, 0), text)
    img2.convert('RGBA')
    img2.putalpha(150)
    img.paste(img2, (0, 0), img2)
    img.save(f'./test/{name}')


