# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pydub import AudioSegment
song = AudioSegment.from_mp3("test.mp3")    # 讀取聲音檔案

# 定義加速與減速的函式
def speed_change(sound, speed=1.0):
    rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
      })
    return rate.set_frame_rate(sound.frame_rate)

song_slow = speed_change(song, 0.75)   # 聲音減速
song_fast = speed_change(song, 2.0)    # 聲音加速

song_slow.export('song_slow.mp3')
song_fast.export('song_fast.mp3')

