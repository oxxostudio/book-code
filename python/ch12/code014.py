# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('oxxostudio.pdf', password='1234')         # 開啟 pdf
pdf_pwd = Pdf.open('oxxostudio-pwd.pdf', password='1234') # 開啟需要密碼的 pdf
print(pdf)
print(pdf_pwd)

