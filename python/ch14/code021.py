# Copyright © https://steam.oxxostudio.tw

import pyaudio
import wave
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import matplotlib.pyplot as plt

chunk = 1024                     # 記錄聲音的樣本區塊大小
sample_format = pyaudio.paInt16  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2                     # 聲道數量
fs = 44100                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
filename = "oxxostudio.wav"      # 錄音檔名

p = pyaudio.PyAudio()            # 建立 pyaudio 物件

# 開啟錄音串流
stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
frames = []                      # 建立聲音串列
run = True                       # 設定開始錄音

fig, ax = plt.subplots()         # 建立單一圖表

# 定義錄音的函式
def record():
    global run, stream, p, frames, wf
    print("錄音開始...")
    while run:
        data = stream.read(chunk)
        frames.append(data)        # 將聲音記錄到串列中
    stream.stop_stream()           # 停止錄音
    stream.close()                 # 關閉串流
    p.terminate()
    print('錄音結束...')
    wf = wave.open(filename, 'wb') # 開啟聲音記錄檔
    wf.setnchannels(channels)      # 設定聲道
    wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
    wf.setframerate(fs)              # 設定取樣頻率
    wf.writeframes(b''.join(frames)) # 存檔
    wf.close()
    visualize(filename)              # 執行畫圖函式

# 定義鍵盤按鍵函式
def keyin():
    global run
    if input() == 'a':
        run = False                # 如果按下 a，就上 run 等於 False

# 定義繪製圖表函式
def visualize(path):
    print('畫圖...')
    raw = wave.open(path)          # 開啟聲音
    signal = raw.readframes(-1)    # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype ="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()    # 取得 framerate
    time = np.linspace(0, len(signal)/f_rate, num = len(signal))  # 根據聲音採樣產生成對應的時間

    ax.plot(time, signal)          # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")        # 圖表標題
    plt.xlabel("Time")             # 橫軸標題
    plt.show()

executor = ThreadPoolExecutor()    # 平行任務處理
e2 = executor.submit(keyin)
e1 = executor.submit(record)
executor.shutdown()

