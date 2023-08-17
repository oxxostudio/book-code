# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment
video = AudioSegment.from_file("oxxostudio.mp4")
output = video[2000:10000]    # 剪輯聲音
output = output[:] + 10       # 放大聲音
output.export('output.mp3')
print('ok')

