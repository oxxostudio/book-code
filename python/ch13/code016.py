# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageOps
bg = Image.new('RGB',(1240, 840), '#000000')   # 因為擴張，所以將尺寸改成 1240x840
for i in range(1,9):
    img = Image.open(f'd{i}.jpg')
    img = img.resize((300, 400))
    img = ImageOps.expand(img, 20, '#ffffff')  # 擴張邊緣，產生邊框
    x = (i-1)%4
    y = (i-1)//4
    bg.paste(img,(x*300, y*400))

bg.save('oxxostudio.jpg')


