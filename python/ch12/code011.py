# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import pdfplumber
pdf = pdfplumber.open('test.pdf', password='12345678')   # 輸入密碼
page = pdf.pages[0]
text = page.extract_text()
print(table)
pdf.close()

