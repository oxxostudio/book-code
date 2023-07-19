# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,10,100,40)
        self.label.setStyleSheet('font-size:30px;')
        self.label.setText('0')

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count)

        self.a = 0

        self.btn_start = QtWidgets.QPushButton(self)
        self.btn_start.setText('開始')
        self.btn_start.setGeometry(20,70,80,30)
        self.btn_start.clicked.connect(self.start)          # 點擊按鈕執行 start()

        self.btn_pause = QtWidgets.QPushButton(self)
        self.btn_pause.setText('暫停')
        self.btn_pause.setGeometry(100,70,80,30)
        self.btn_pause.clicked.connect(self.pause)          # 點擊按鈕執行 pause()

        self.btn_reset = QtWidgets.QPushButton(self)
        self.btn_reset.setText('重設')
        self.btn_reset.setGeometry(180,70,80,30)
        self.btn_reset.clicked.connect(self.reset)          # 點擊按鈕執行 reset()

    def count(self):
        self.a = self.a + 1
        self.label.setText(str(self.a))

    def start(self):
        self.timer.start(500)          # 啟用定時器

    def pause(self):
        self.timer.stop()              # 停止定時器

    def reset(self):
        self.a = 0                     # 數值歸零
        self.label.setText('0')
        self.timer.stop()              # 停止定時器

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

