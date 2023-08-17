# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組
song = AudioSegment.from_mp3("oxxostudio.mp3")    # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")       # 輸出為 wav
print('ok')                                       # 輸出後印出 ok

