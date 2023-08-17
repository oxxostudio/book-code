# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.fade_in(3000)     # 開頭三秒 ( 3000ms ) 淡入
output2 = song.fade_out(3000)    # 結尾三秒 ( 3000ms ) 淡出
output1.export('output1.mp3')
output2.export('output2.mp3')
print('ok')

