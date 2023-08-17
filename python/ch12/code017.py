# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('oxxostudio.pdf')
pages = pdf.pages
n = 1
for i in pages:
    output = Pdf.new()
    output.pages.append(i)
    output.save(f'new_{n}.pdf')    # 格式化檔案名稱
    n = n + 1                      # 編號加 1


