# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('oxxosudio.pdf')   # 開啟 pdf
del pdf.pages[1:2]                # 刪除第二頁
pdf.save('output.pdf')


