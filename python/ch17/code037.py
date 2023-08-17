# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用

from pytube import Playlist, YouTube
playlist = Playlist('https://www.youtube.com/watch?v=mOPRaLPh-YU&list=PL9ACDjBMkp9wViVmgpYweGkNqh62pHspF')
print('download...')
for i in playlist.video_urls:
    print(i)
    yt = YouTube(i)                                           # 讀取影片
    yt.streams.filter().get_highest_resolution().download()   # 下載為最高畫質影片
print('ok!')
