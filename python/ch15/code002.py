# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

format_list = ['avi','mov','wmv','flv','asf', 'mkv']

for n in range(3):
    video = VideoFileClip(f"oxxo_{n}.mp4")  # 使用 for 迴圈讀取影片
    for i in format_list:
        output = video.copy()
        output.write_videofile(f"output_{n}.{i}",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

