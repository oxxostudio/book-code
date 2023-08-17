# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=R93ce4FZGbc')
print('download...')
yt.streams.filter().get_by_resolution('360p').download(filename='oxxostudio_360p.mp4')
# 下載 480p 的影片畫質
print('ok!')

