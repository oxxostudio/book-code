# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from barcode import EAN13
from barcode.writer import ImageWriter         # 載入 barcode.writer 的 ImageWriter

number = '12345678987654321'
my_code = EAN13(number, writer=ImageWriter())  # 添加 writer=ImageWriter()
my_code.save("oxxo")

