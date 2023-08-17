# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])
# 建立字典對照表
info = {
    '0th':[271, 272, 282, 283, 305, 306, 316],
    'Exif':[33434, 33437, 34855, 36867, 36868, 36880, 36881, 36882, 40962, 40963, 42035 ,42036],
    '1st':[282, 283],
    'GPS':[2, 4, 5, 17, 24, 31]
}
# 根據對照表，印出照片 exif 裡的資訊 ( 有就印出，沒有就略過 )
for i in info:
    for j in info[i]:
        if j in exif[i]:
            print(j, ':', exif[i][j])


