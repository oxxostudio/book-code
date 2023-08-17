# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])

exif["0th"][305] = b'OXXO.STUDIO'          # 修改編輯軟體
exif["0th"][306] = b'2020:01:01 00:00:00'  # 修改編輯時間
exif["Exif"][36867] = b'2020:01:01 00:00:00'   # 加入檔案建立時間
exif["Exif"][36868] = b'2020:01:01 00:00:00'   # 加入檔案建立時間
exif_new = piexif.dump(exif)               # 更新 Exif
img.save("./iphone-edit.jpg", exif = exif_new )  # 另存新檔並加入 Exif


