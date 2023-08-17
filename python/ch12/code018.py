# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('test.pdf')
pages = pdf.pages
output = Pdf.new()
output.pages.extend(pages[1:3])   # 改用 extend，放入特定範圍的頁面
output.save('new.pdf')


