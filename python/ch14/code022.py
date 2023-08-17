# Copyright © https://steam.oxxostudio.tw

import numpy as np

samplerate = 44100    # 取樣頻率

def get_wave(freq, duration=0.5):
    amplitude = 4096      # 震幅 ( 音量大小 )
    t = np.linspace(0, duration, int(samplerate * duration)) # 使用等差級數，在指定時間長度裡，根據取樣頻率建立區間
    wave = amplitude * np.sin(2 * np.pi * freq * t)          # 在每個區間裡放入指定頻率的波形
    return wave

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']  # 建立音符英文字對照表
    base_freq = 261.63    # 預設為 C4 的頻率
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))} # 產生頻率和英文字的對照
    note_freqs[''] = 0.0  # 如果是空值則為 0 ( 無聲音 )
    return note_freqs

def get_song_data(music_notes):
    note_freqs = get_piano_notes()   # 取的英文與音符對照表
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]  # 根據音樂的音符，對應到對照表產生指定串列
    song = np.concatenate(song)      # 連接為新陣列
    return song

# 音樂的音符表
music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
data = get_song_data(music_notes)   # 轉換成頻率對照表
data = data * (16300/np.max(data))  # 調整震幅 ( 音量大小 )

from scipy.io.wavfile import write
write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))  # 寫入檔案

