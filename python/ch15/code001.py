# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")    # 讀取影片

format_list = ['avi','mov','wmv','flv','asf', 'mkv']  # 要轉換的格式清單

# 使用 for 迴圈轉換成所有格式
for i in format_list:
    output = video.copy()
    output.write_videofile(f"output.{i}",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')
