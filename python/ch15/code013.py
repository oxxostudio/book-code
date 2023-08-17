# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *
v1 = VideoFileClip("oxxo1.mp4")           # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")           # 讀取影片
v1 = mask_color(v1,color=0,thr=10,s=0)    # 設定 v1 遮罩為半透明
                                          # color=0 表示黑色，thr 和 s 是參數，這種設定為半透明
output = CompositeVideoClip([v2,v1])      # 混合影片
output.write_videofile("output.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')

