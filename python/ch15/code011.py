# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
v1 = VideoFileClip("oxxo1.mp4")         # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")         # 讀取影片
v3 = VideoFileClip("oxxo3.mp4")         # 讀取影片
v4 = VideoFileClip("oxxo4.mp4")         # 讀取影片
v1 = v1.resize((480,360)).margin(10)    # 改變尺寸，增加邊界
v2 = v2.resize((480,360)).margin(10)    # 改變尺寸，增加邊界
v3 = v3.resize((480,360)).margin(10)    # 改變尺寸，增加邊界
v4 = v4.resize((480,360)).margin(10)    # 改變尺寸，增加邊界
output = clips_array([[v1,v2],[v3,v4]]) # 排列影片，v1 和 v2 一組，v3 和 v4 一組
output.write_videofile("output.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print('ok')

