# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import pdfplumber
pdf = pdfplumber.open('oxxostudio.pdf')   # 開啟 pdf
print(pdf.pages)                          # [<Page:1>, <Page:2>, <Page:3>]，共有三頁


