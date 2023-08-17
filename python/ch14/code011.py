# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")

output1 = song.fade(to_gain=15, start=1000, duration=2000)
# 從 1 秒的位置開始，慢慢變大聲到增加 15，過程持續 2 秒

output2 = song.fade(to_gain=-30, end=3000, duration=2000)
# 從 1 秒的位置開始 ( 3000-2000 )，慢慢變小聲到減少 30，過程持續 2 秒

output1.export('output1.mp3')
output2.export('output2.mp3')
print('ok')

