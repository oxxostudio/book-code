# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf1 = Pdf.open('oxxo_1.pdf')        # 讀取第一份 pdf
pdf2 = Pdf.open('oxxo_2.pdf')        # 讀取第二份 pdf
pdf3 = Pdf.open('oxxo_3.pdf')        # 讀取第三份 pdf

output = Pdf.new()                   # 建立新的 pdf 物件
output.pages.append(pdf1.pages[0])   # 添加第一頁到第一份
output.pages.append(pdf2.pages[0])   # 添加第一頁到第二份
output.pages.append(pdf3.pages[0])   # 添加第一頁到第三份
output.save('output.pdf')


