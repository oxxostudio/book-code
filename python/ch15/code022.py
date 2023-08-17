# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
video = VideoFileClip("oxxostudio.mp4")
output_1 = lum_contrast(video, lum=-50, contrast=0)    # 亮度減少 50
output_2 = lum_contrast(video, lum=150, contrast=0)    # 亮度增加 150
output_3 = lum_contrast(video, lum=0, contrast=-0.5)   # 對比減少 0.5
output_4 = lum_contrast(video, lum=0, contrast=2)      # 對比增加 2

output_1.write_videofile("output_1.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_2.write_videofile("output_2.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_3.write_videofile("output_3.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_4.write_videofile("output_4.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

