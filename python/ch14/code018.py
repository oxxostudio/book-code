# Copyright © https://steam.oxxostudio.tw

import pyaudio
import wave
from pydub import AudioSegment            # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play           # 載入 pydub.playback 的 play 模組

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 5
filename = "oxxostudio.wav"

p = pyaudio.PyAudio()

print("開始錄音...")

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print('錄音結束...')

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

song = AudioSegment.from_mp3("song.mp3")        # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_wav("oxxostudio.wav") # 讀取錄音 wav 檔案
output = voice.overlay(song, loop=True)         # 混合錄音和背景音樂
play(output)                                    # 播放聲音
output.export('output.mp3')                     # 輸出為 mp3
print('ok')

