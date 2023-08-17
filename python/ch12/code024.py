# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('output.pdf')
pdf.pages.reverse()           # 反轉 pdf
pdf.save('output2.pdf')

