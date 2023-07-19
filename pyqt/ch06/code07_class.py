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
        now = QtCore.QTime.currentTime()   # 取得目前電腦時間

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,20,120,30)

        self.t1 = QtWidgets.QTimeEdit(self)
        self.t1.setGeometry(140,20,120,30)
        self.t1.setDisplayFormat('hh:mm:ss')
        self.t1.setTime(now)                    # 設定時間
        self.t1.setTimeRange(QtCore.QTime(3, 00, 00), QtCore.QTime(23, 30, 00))
        self.t1.timeChanged.connect(self.showTime)

    def showTime(self):
        self.label.setText(self.t1.time().toString())  # 顯示時間

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

