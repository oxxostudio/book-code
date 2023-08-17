# Copyright © https://steam.oxxostudio.tw


import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

img1 = ImageClip("oxxo1.jpg", transparent=True).set_duration(3)
img2 = ImageClip("oxxo2.jpg", transparent=True).set_duration(4).set_start(2).crossfadein(1)
img3 = ImageClip("oxxo3.jpg", transparent=True).set_duration(3).set_start(5).crossfadein(1)

output = CompositeVideoClip([img1,img2,img3])

output.write_videofile("output.mp4",fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')