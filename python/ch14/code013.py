# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment                      # 載入 pydub 的 AudioSegment 模組
voice = AudioSegment.from_mp3("voice.mp3")          # 讀取說話聲音 mp3 檔案
output = voice.reverse()                            # 反轉說話聲音
output.export('output.mp3')

