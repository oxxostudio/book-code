# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment
song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
output = song*3                                 # 乘以 3，重複三次變成三倍長
output.export('output.mp3')
print('ok')

