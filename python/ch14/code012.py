# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment                      # 載入 pydub 的 AudioSegment 模組
song = AudioSegment.from_mp3("oxxostudio.mp3")      # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_mp3("voice.mp3")          # 讀取說話聲音 mp3 檔案
output = voice.overlay(song, loop=True)             # 混合說話聲音和背景音樂
output.export('output.mp3')

