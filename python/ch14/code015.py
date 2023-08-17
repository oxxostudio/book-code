# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment            # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play           # 載入 pydub.playback 的 play 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 開啟聲音檔案
output = song*2                                 # 讓聲音檔案變成兩倍長
play(output)                                    # 播放聲音

