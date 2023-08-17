# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")   # 讀取影片
audio = video.audio                       # 取出聲音
audio.write_audiofile("song.mp3")         # 輸出聲音為 mp3
print('ok')

