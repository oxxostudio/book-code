# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import qrcode
img = qrcode.make('https://steam.oxxostudio.tw')    # 要轉換成 QRCode 的文字
img.show()                # 顯示圖片 ( Colab 不適用 )
img.save('qrcode.png')    # 儲存圖片

