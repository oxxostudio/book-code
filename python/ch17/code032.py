# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=R93ce4FZGbc')
print(yt.streams.all())

