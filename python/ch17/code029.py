# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=R93ce4FZGbc')   # baby shark 的音樂
print(yt.title)           # 影片標題
print(yt.length)          # 影片長度 ( 秒 )
print(yt.author)          # 影片作者
print(yt.channel_url)     # 影片作者頻道網址
print(yt.thumbnail_url)   # 影片縮圖網址
print(yt.views)           # 影片觀看數
