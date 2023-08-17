# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.subclip(12,15)                 # 剪輯影片 ( 單位秒 )
output.write_videofile("output_1.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print('ok')

