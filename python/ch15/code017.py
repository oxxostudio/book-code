# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
video = VideoFileClip("oxxostudio.mp4")
output_1 = crop(video, x1=10, y1=10, width=50, height=50)  # 方法 1，指定左上 (x1, y1) 座標和寬高
output_2 = crop(video, x1=10, y1=10, x2=50, y2=50)         # 方法 2，指定左上 (x1, y1) 座標和右下 ( x2, y2 )座標
output_3 = crop(video, x1=10, width=100)                   # 方法 3，指定左上 x1 座標和寬度，就會自動採用 y1=0 和影片高度

output_1.write_videofile("output.mp4", fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')

