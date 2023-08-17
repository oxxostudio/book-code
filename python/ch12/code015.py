# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

from pikepdf import Pdf, Permissions, Encryption
pdf = Pdf.open('oxxostudio-pwd.pdf', password='1234')    # 開啟密碼為 1234 的 pdf
no_extracting = Permissions(extract=False)
# 儲存為密碼是 qqqq 的 pdf
pdf.save('new.pdf', encryption = Encryption(user="qqqq", owner="qqqq", allow=no_extracting))

