# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://steam.oxxostudio.tw')   # 要轉換成 QRCode 的文字
qr.make(fit=True)          # 根據參數製作為 QRCode 物件

img = qr.make_image()      # 產生 QRCode 圖片
img.show()                 # 顯示圖片 ( Colab 不適用 )
img.save('qrcode.png')     # 儲存圖片

