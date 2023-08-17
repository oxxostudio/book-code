# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
video = VideoFileClip("oxxostudio.mp4")
frame = video.save_frame("frame1.jpg", t = 22)
frame = video.save_frame("frame2.jpg", t = 22.1)
frame = video.save_frame("frame3.jpg", t = 22.2)
print('ok')

