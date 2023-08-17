# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import pdfplumber
pdf = pdfplumber.open('oxxostudio.pdf')
page = pdf.pages[0]           # 讀取第一頁
text = page.extract_text()    # 取出文字
print(text)


