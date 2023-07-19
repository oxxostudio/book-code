# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore, QtMultimedia
import sys, os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.playMusic()

    def playMusic(self):
        self.player = QtMultimedia.QMediaPlayer()        # 建立播放器
        self.path = os.getcwd() + '/'                    # 取得目前工作路徑
        self.qurl = QtCore.QUrl.fromLocalFile(self.path+'test.mp3')  # 取得音樂路徑
        self.audio_output = QtMultimedia.QAudioOutput()  # 建立音樂輸出器

        self.player.setAudioOutput(self.audio_output)    # PyQt6 播放器與音樂輸出器綁定
        self.player.setSource(self.qurl)                 # PyQt6 建立音樂內容
        # self.qmusic = QtMultimedia.QMediaContent(self.qurl) # PyQt5 建立音樂內容
        # self.player.setMedia(self.qmusic)                   # PyQt5 將播放器與音樂內容綁定


        self.audio_output.setVolume(100)                 # 設定音量
        self.player.play()                               # 播放

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

