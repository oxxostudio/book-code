# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from barcode import EAN13

number = '12345678987654321'  # 要轉換的數字
my_code = EAN13(number)       # 轉換成 barcode
my_code.save("oxxo")          # 儲存為 SVG

