# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
video = VideoFileClip("oxxostudio.mp4")     # 讀取影片
output_1 = speedx(video, factor=2)          # 2 倍速
output_2 = speedx(video, factor=0.5)        # 0.5 倍速
output_3 = speedx(video, final_duration=2)  # 將影片變成 2 秒長

output_1.write_videofile("output_1.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_2.write_videofile("output_2.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_3.write_videofile("output_3.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

