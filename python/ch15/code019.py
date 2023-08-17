# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
video = VideoFileClip("oxxostudio.mp4")
output_x = mirror_x(video)    # 左右翻轉
output_y = mirror_y(video)    # 垂直翻轉

output_x.write_videofile("output_x.mp4", fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_y.write_videofile("output_y.mp4", fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

