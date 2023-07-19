# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,10,100,40)
label.setStyleSheet('font-size:30px;')
label.setText('0')

a = 0
def count():
    global a
    a = a + 1
    label.setText(str(a))

timer = QtCore.QTimer()
timer.timeout.connect(count)

def start():
    timer.start(500)          # 啟用定時器

def pause():
    timer.stop()              # 停止定時器

def reset():
    global a
    a = 0                     # 數值歸零
    label.setText('0')
    timer.stop()              # 停止定時器

btn_start = QtWidgets.QPushButton(Form)
btn_start.setText('開始')
btn_start.setGeometry(20,70,80,30)
btn_start.clicked.connect(start)          # 點擊按鈕執行 start()

btn_pause = QtWidgets.QPushButton(Form)
btn_pause.setText('暫停')
btn_pause.setGeometry(100,70,80,30)
btn_pause.clicked.connect(pause)          # 點擊按鈕執行 pause()

btn_reset = QtWidgets.QPushButton(Form)
btn_reset.setText('重設')
btn_reset.setGeometry(180,70,80,30)
btn_reset.clicked.connect(reset)          # 點擊按鈕執行 reset()

Form.show()
sys.exit(app.exec())

