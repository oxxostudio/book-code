# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import pdfplumber
pdf = pdfplumber.open('oxxostudio.pdf')
page = pdf.pages[1]           # 讀取第二頁
table = page.extract_table()  # 取出表格
print(table)
pdf.close()

