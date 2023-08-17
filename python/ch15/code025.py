# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")
output = video.resize((360,180))
output = output.subclip(13,15)
output.write_gif("output_fps24.gif", fps=24)               # 256 色一秒 24 格
output.write_gif("output_fps8.gif", fps=8)                 # 256 色一秒 8 格
output.write_gif("output_fps8_c2.gif", fps=8, colors=2)    # 2 色一秒 8 格
output.write_gif("output_fps8_c16.gif", fps=8, colors=16)  # 16 色一秒 8 格
print('ok')

