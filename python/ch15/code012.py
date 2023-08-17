# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
v1 = VideoFileClip("oxxo1.mp4")          # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")          # 讀取影片
output = CompositeVideoClip([v2,v1])     # 混合影片
output.write_videofile("output.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print('ok')

