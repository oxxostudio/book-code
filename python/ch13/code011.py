# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
img = Image.open('./oxxostudio.jpg')      # 開啟圖片
img_crop = img.crop((0,0,200,100))        # 裁切圖片
img_crop.save('./test.jpg')               # 存檔
# img_crop.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器

