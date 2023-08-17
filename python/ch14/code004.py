# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組
song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
duration = song.duration_seconds                # 讀取長度
channels = song.channels                        # 讀取聲道數量
print(channels, duration)                       # 印出資訊

