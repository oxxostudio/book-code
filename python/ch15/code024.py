# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.resize((360, 180))        # 壓縮影片
output = output.subclip(13, 15)          # 取出 13～15 秒的片段
output.write_gif("output.gif")           # 將這個片段轉換成 gif
print('ok')

