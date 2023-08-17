# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFont, ImageDraw
img = Image.open('./photo.jpg')    # 開啟圖片
font = ImageFont.truetype('Teko-Regular.ttf', 100)   # 設定字型
draw = ImageDraw.Draw(img)     # 準備在圖片上繪圖
draw.text((0,0), 'OXXO.STUDIO', fill=(255,255,255), font=font)  # 將文字畫入圖片
img.save('./ok.jpg')     # 儲存圖片
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


