# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *
import sys, os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()
        self.run()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('0.0 / 0.0')
        self.label.setGeometry(210, 30, 100, 30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('播放')
        self.btn1.setGeometry(25, 30, 60, 30)
        self.btn1.setDisabled(True)
        self.btn1.clicked.connect(self.f1)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('暫停')
        self.btn2.setGeometry(75, 30, 60, 30)
        self.btn2.clicked.connect(self.f2)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText('停止')
        self.btn3.setGeometry(125, 30, 60, 30)
        self.btn3.clicked.connect(self.f3)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setGeometry(30, 60, 240, 30)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.sliderMoved.connect(lambda: self.player.setPosition(self.slider.value()))

        self.player = QMediaPlayer()             # 設定播放器
        self.path = os.getcwd()                  # 取得音樂檔案路徑
        self.qurl = QUrl.fromLocalFile(self.path+'/test.mp3') # 轉換成 QUrl
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)         # 播放器與音樂輸出器綁定
        self.player.setSource(self.qurl)
        self.player.durationChanged.connect(lambda: self.slider.setMaximum(self.player.duration()))
        self.player.play()

    def f1(self):
        self.btn1.setDisabled(True)
        self.btn2.setDisabled(False)
        self.btn3.setDisabled(False)
        self.player.play()

    def f2(self):
        self.btn1.setDisabled(False)
        self.btn2.setDisabled(True)
        self.btn3.setDisabled(False)
        self.player.pause()

    def f3(self):
        self.btn1.setDisabled(False)
        self.btn2.setDisabled(False)
        self.btn3.setDisabled(True)
        self.player.stop()

    def playmusic(self):
        progress = self.player.position()
        self.slider.setValue(progress)
        self.label.setText(f'{str(round(progress/1000, 1))} / {str(round(self.player.duration()/1000, 1))}')

    def run(self):
        self.timer = QTimer()               # 加入定時器
        self.timer.timeout.connect(self.playmusic)   # 設定定時要執行的 function
        self.timer.start(1000)              # 啟用定時器，設定間隔時間為 500 毫秒

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

