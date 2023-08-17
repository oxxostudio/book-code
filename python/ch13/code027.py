# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('oxxostudio.jpg')
w,h = img.size
level = 20
img2 = img.resize((int(w/level),int(h/level)))
img2 = img2.resize((w,h), resample = Image.NEAREST)

x1, y1 = 60, 60                  # 定義選取區域的左上角座標
x2, y2 = 250, 250                # 定義選取區域的右上角座標
area = img2.crop((x1,y1,x2,y2))  # 裁切區域
img.paste(area,(x1, y1))         # 在原本的圖片裡貼上馬賽克區域
img.save('test.jpg')


