# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf1 = Pdf.open('oxxostudio.pdf')    # 開啟第一份 pdf
pdf2 = Pdf.open('new.pdf')           # 開啟第二份 pdf
pdf1.pages.insert(1, pdf2.pages[0])  # 在第一份的第一頁後方，插入第二份的第一頁
pdf1.save('output.pdf')


