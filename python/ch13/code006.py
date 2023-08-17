# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('oxxostudio.jpg')   # 開啟圖片
img2 = img.resize((200,200))         # 調整圖片尺寸為 200x200
img2.save('test.jpg')                # 調整後存檔到 resize 資料夾

