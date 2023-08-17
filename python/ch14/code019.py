# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

import matplotlib.pyplot as plt
import numpy as np
import wave

fig, ax = plt.subplots()  # 建立單一圖表

# 建立繪製聲波的函式
def visualize(path):
    raw = wave.open(path)          # 開啟聲音
    signal = raw.readframes(-1)    # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype ="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()    # 取得 framerate
    time = np.linspace(0, len(signal)/f_rate, num = len(signal))  # 根據聲音採樣產生成對應的時間

    ax.plot(time, signal)          # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")        # 圖表標題
    plt.xlabel("Time")             # 橫軸標題
    plt.show()

visualize('oxxostudio.wav')        # 讀取聲音

