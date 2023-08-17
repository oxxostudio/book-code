# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf1 = Pdf.open('oxxo_more_1.pdf')   # 讀取第一份多頁面 pdf
pdf2 = Pdf.open('oxxo_more_2.pdf')   # 讀取第一份多頁面 pdf
pdf3 = Pdf.open('oxxo_more_1.pdf')   # 讀取第一份多頁面 pdf

output = Pdf.new()
output.pages.extend(pdf1.pages)      # 添加所有頁面到第一份
output.pages.extend(pdf2.pages)      # 添加所有頁面到第二份
output.pages.extend(pdf3.pages)      # 添加所有頁面到第三份
output.save('output.pdf')


