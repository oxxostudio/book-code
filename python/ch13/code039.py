# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import pytesseract

img = Image.open('chinese.jpg')
text = pytesseract.image_to_string(img, lang='chi_tra')
print(text)


