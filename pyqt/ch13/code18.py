# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys, os

app = QtWidgets.QApplication(sys.argv)
main = QtWidgets.QMainWindow()
main.setObjectName("MainWindow")
main.setWindowTitle("oxxo.studio")
main.resize(300, 300)

label = QtWidgets.QLabel(main)        # 放入 QLabel 顯示時間
label.setGeometry(210, 30, 100, 30)   # 設定位置
label.setText('0.0 / 0.0')            # 預設顯示文字

# 點擊播放按鈕的程式
def f1():
    btn1.setDisabled(True)     # 停用播放按鈕
    btn2.setDisabled(False)    # 啟用暫停按鈕
    btn3.setDisabled(False)    # 啟用停止按鈕
    player.play()              # 播放聲音

# 點擊暫停按鈕的程式
def f2():
    btn1.setDisabled(False)    # 啟用播放按鈕
    btn2.setDisabled(True)     # 停用暫停按鈕
    btn3.setDisabled(False)    # 啟用停止按鈕
    player.pause()             # 暫停聲音

# 點擊停止按鈕的程式
def f3():
    btn1.setDisabled(False)    # 啟用播放按鈕
    btn2.setDisabled(False)    # 啟用暫停按鈕
    btn3.setDisabled(True)     # 停用停止按鈕
    player.stop()              # 停止聲音

btn1 = QtWidgets.QPushButton(main)  # 放入播放按鈕
btn1.setText('播放')                 # 設定文字
btn1.setGeometry(25, 30, 60, 30)    # 設定位置
btn1.setDisabled(True)              # 預設停用
btn1.clicked.connect(f1)            # 連接 f1 程式

btn2 = QtWidgets.QPushButton(main)  # 放入暫停按鈕
btn2.setText('暫停')                 # 設定文字
btn2.setGeometry(75, 30, 60, 30)    # 設定位置
btn2.clicked.connect(f2)            # 連接 f2 程式

btn3 = QtWidgets.QPushButton(main)  # 放入停止按鈕
btn3.setText('停止')                 # 設定文字
btn3.setGeometry(125, 30, 60, 30)   # 設定位置
btn3.clicked.connect(f3)            # 連接 f3 程式

slider = QtWidgets.QSlider(main)    # 放入調整滑桿
slider.setOrientation(1)            # 設定水平顯示
slider.setGeometry(30, 60, 240, 30) # 設定位置
slider.setRange(0, 100)             # 設定預設範圍
slider.setValue(50)                 # 設定預設值
slider.sliderMoved.connect(lambda: player.setPosition(slider.value())) # 當滑桿移動時，設定播放器的播放位置

player = QMediaPlayer()             # 設定播放器
path = os.getcwd()                  # 取得音樂檔案路徑
qurl = QUrl.fromLocalFile(path+'/test.mp3') # 轉換成 QUrl
music = QMediaContent(qurl)         # 讀取音樂
player.setMedia(music)              # 設定播放音樂
player.durationChanged.connect(lambda: slider.setMaximum(player.duration())) # 當總長度改變時，設定滑桿的最大值
player.play()                       # 播放音樂

# 播放器的函式
def playmusic():
    progress = player.position()    # 取的目前播放時間
    slider.setValue(progress)       # 設定滑桿位置
    label.setText(f'{str(round(progress/1000, 1))} / {str(round(player.duration()/1000, 1))}') # 文字顯示

timer = QTimer()                    # 加入定時器
timer.timeout.connect(playmusic)    # 設定定時要執行的 function
timer.start(1000)                   # 啟用定時器，設定間隔時間為 500 毫秒

main.show()
sys.exit(app.exec_())

