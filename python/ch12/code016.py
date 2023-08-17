# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf
pdf = Pdf.open('oxxostudio.pdf')   # 開啟 pdf
pages = pdf.pages                  # 將每一頁的內容變成串列
output = Pdf.new()                 # 建立新的 pdf 物件
output.pages.append(pages[0])      # 添加頁面內容
output.save('new.pdf')             # 儲存為新的 pdf


