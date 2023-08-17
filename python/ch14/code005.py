# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song[1500:5500].export('output.mp3')            # 取出 1500 毫秒～5500 毫秒長度的聲音，輸出為 output.mp3
print('ok')                                     # 輸出後印出 ok

