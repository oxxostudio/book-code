# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3
output1 = song[:] + 10                          # 將所有陣列中的資料增加 10 ( 變大聲 )
output2 = song[:] - 10                          # 將所有陣列中的資料減少 10 ( 變小聲 )
output1.export('output1.mp3')                   # 輸出聲音
output2.export('output2.mp3')
print('ok')

