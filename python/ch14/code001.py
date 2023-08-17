# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment
song = AudioSegment.from_mp3("oxxostudio.mp3")      # 讀取 mp3 檔案
print(song)     # <pydub.audio_segment.AudioSegment object at 0x7faaa545a7f0>

