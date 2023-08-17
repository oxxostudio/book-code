# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")
brightness = ImageEnhance.Brightness(img) # 調整亮度
contrast = ImageEnhance.Contrast(img)     # 調整對比
color = ImageEnhance.Color(img)           # 調整飽和度
sharpness = ImageEnhance.Sharpness(img)   # 調整銳利度

output_b5 = brightness.enhance(5)         # 提高亮度
output_b05 = brightness.enhance(0.5)      # 降低亮度
output_c5 = contrast.enhance(5)           # 提高對比
output_c05 = contrast.enhance(0.5)        # 降低對比
output_color5 = color.enhance(5)          # 提高飽和度
output_color01 = color.enhance(0.1)       # 降低飽和度
output_s15 = sharpness.enhance(15)        # 提高銳利度
output_s0 = sharpness.enhance(0)          # 降低銳利度

plt.figure(figsize=(15,10))          # 改變圖表尺寸
plt.subplot(241)                     # 建立 4x2 子圖表的上方從左數來第一個圖表
plt.imshow(output_b5)
plt.title('brightness:5')
plt.subplot(242)                     # 建立 4x2 子圖表的上方從左數來第二個圖表
plt.imshow(output_b05)
plt.title('brightness:0.5')
plt.subplot(243)                     # 建立 4x2 子圖表的上方從左數來第三個圖表
plt.imshow(output_c5)
plt.title('contrast:5')
plt.subplot(244)                     # 建立 4x2 子圖表的上方從左數來第四個圖表
plt.imshow(output_c05)
plt.title('contrast:0.5')
plt.subplot(245)                     # 建立 4x2 子圖表的下方從左數來第一個圖表
plt.imshow(output_color5)
plt.title('color:5')
plt.subplot(246)                     # 建立 4x2 子圖表的下方從左數來第二個圖表
plt.imshow(output_color01)
plt.title('color:0.1')
plt.subplot(247)                     # 建立 4x2 子圖表的下方從左數來第三個圖表
plt.imshow(output_s15)
plt.title('sharpness:15')
plt.subplot(248)                     # 建立 4x2 子圖表的下方從左數來第四個圖表
plt.imshow(output_s0)
plt.title('sharpness:0')

plt.show()

