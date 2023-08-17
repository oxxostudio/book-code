# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment                 # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3") # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")    # 轉換並儲存為 wav

fig, ax = plt.subplots()

def visualize(path):
    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    f_rate = raw.getframerate()
    time = np.linspace(0, len(signal)/f_rate, num = len(signal))

    ax.plot(time, signal)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.show()

visualize('oxxostudio.wav')

