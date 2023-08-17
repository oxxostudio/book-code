# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment

song1 = AudioSegment.from_mp3("oxxo1.mp3")  # 讀取第一個 mp3 檔案
song2 = AudioSegment.from_mp3("oxxo2.mp3")  # 讀取第二個 mp3 檔案
output = song1 + song2                      # 串接兩段聲音
output.export('output.mp3')                 # 輸出為 output.mp3
print('ok')                                 # 輸出後印出 ok

