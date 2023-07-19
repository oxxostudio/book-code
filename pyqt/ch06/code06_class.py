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
        self.t1 = QtWidgets.QTimeEdit(self)
        self.t1.setGeometry(20,20,120,30)
        self.t1.setDisplayFormat('hh:mm:ss')
        self.t1.setTimeRange(QtCore.QTime(10, 00, 00), QtCore.QTime(20, 00, 00))  # 設定時間範圍

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

