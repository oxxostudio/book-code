# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
o1 = VideoFileClip("oxxo1.mp4")                    # 開啟第一段影片
o2 = VideoFileClip("oxxo2.mp4")                    # 開啟第二段影片
o3 = VideoFileClip("oxxo3.mp4")                    # 開啟第三段影片
output = concatenate_videoclips([o1, o2, o3])      # 合併影片
output.write_videofile("output123.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')
