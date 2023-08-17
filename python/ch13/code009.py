# Copyright © https://steam.oxxostudio.tw

from PIL import Image, ImageEnhance
img = Image.open("oxxostudio.jpg")         # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(1.5)           # 提高亮度
output.save('oxxostudio_b15.jpg')          # 存檔

output = brightness.enhance(0.5)           # 降低亮度
output.save('oxxostudio_b05.jpg')          # 存檔

