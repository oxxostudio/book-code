# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
video = VideoFileClip("oxxostudio.mp4")
output_1 = colorx(video, 1.5)     # 調整顏色
output_2 = gamma_corr(video, 1)   # 調整 gamma 值
output_3 = blackwhite(video)      # 黑白影片
output_4 = invert_colors(video)   # 負片效果

output_1.write_videofile("output_1.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_2.write_videofile("output_2.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_3.write_videofile("output_3.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
output_4.write_videofile("output_4.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

