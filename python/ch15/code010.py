# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
o1 = VideoFileClip("oxxo1.mp4")
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3], method='compose')   # 設定 method 為 compose
output.write_videofile("output456.mp4", fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')

