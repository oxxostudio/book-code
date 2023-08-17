# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
audio = AudioFileClip("song.mp3")        # 讀取音樂

output = video2.set_audio(audio)         # 合併影片與聲音
output.write_videofile("output.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
# 注意要設定相關參數，不然轉出來的影片會沒有聲音
print('ok')

