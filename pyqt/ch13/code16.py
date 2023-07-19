# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *
import sys, os

app = QtWidgets.QApplication(sys.argv)
main = QtWidgets.QMainWindow()
main.setObjectName("MainWindow")
main.setWindowTitle("oxxo.studio")
main.resize(300, 300)

player = QMediaPlayer()                     # 建立播放器
path = os.getcwd() + '/'                    # 取得目前工作路徑
qurl = QUrl.fromLocalFile(path+'test.mp3')  # 取得音樂路徑
audio_output = QAudioOutput()               # 建立音樂輸出器

player.setAudioOutput(audio_output)         # PyQt6 播放器與音樂輸出器綁定
player.setSource(qurl)                      # PyQt5 建立音樂內容
# qmusic = QMediaContent(qurl)              # PyQt5 建立音樂內容
# player.setMedia(qmusic)                   # PyQt5 將播放器與音樂內容綁定

audio_output.setVolume(100)                 # 設定音量
player.play()                               # 播放

main.show()
sys.exit(app.exec())

