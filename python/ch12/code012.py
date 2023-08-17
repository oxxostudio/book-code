# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import pdfplumber
pdf = pdfplumber.open('oxxostudio.pdf')
page = pdf.pages[0]
text = page.extract_text()
print(text)
pdf.close()

f = open('test.txt','w+')   # 使用 w+ 模式開啟 test.txt
f.write(text)               # 寫入內容
f.close()                   # 關閉 test.txt


