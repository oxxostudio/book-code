# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks') # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment                     # 載入 pydub 的 AudioSegment 模組
video = AudioSegment.from_file("oxxostudio.mp4")   # 讀取 mp4 檔案
output.export('video.mp3')                         # 講讀取的聲音輸出為 mp3
print('ok')

