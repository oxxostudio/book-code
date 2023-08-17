# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
bg = Image.new('RGB',(400, 300), '#ff0000')         # 產生 RGB 色域，400x300 背景紅色的圖片
bg.save('oxxostudio.jpg')
# bg.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器

