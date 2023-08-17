# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter
img = Image.open('oxxostudio.jpg')         # 開啟圖片
output = img.filter(ImageFilter.SHARPEN)   # 套用圖片銳利化
output.save('output.jpg')                  # 存檔
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


