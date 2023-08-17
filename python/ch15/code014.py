# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
clip_1 = video.subclip(2,5)              # 裁切出三秒影片
clip_2 = video.subclip(17,21).set_start(2).crossfadein(1)  # 裁切出四秒影片，設定兩秒後再開始，淡入一秒
clip_3 = video.subclip(50,53).set_start(5).crossfadein(1)  # 裁切出三秒影片，設定五秒後再開始，淡入一秒

output = CompositeVideoClip([clip_1,clip_2,clip_3])

output.write_videofile("output.mp4", fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')

