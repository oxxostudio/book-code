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
        now = QtCore.QTime.currentTime()

        self.t1 = QtWidgets.QTimeEdit(self)
        self.t1.setGeometry(20,20,120,30)
        self.t1.setDisplayFormat('hh:mm:ss')   # 24 小時制
        self.t1.setTime(now)

        self.t2 = QtWidgets.QTimeEdit(self)
        self.t2.setGeometry(20,60,120,30)
        self.t2.setDisplayFormat('hh:mm ap')   # 上午下午制，上午下午在後面
        self.t2.setTime(now)

        self.t3 = QtWidgets.QTimeEdit(self)
        self.t3.setGeometry(20,100,120,30)
        self.t3.setDisplayFormat('ap hh:mm:ss')  # 上午下午制，上午下午在前面
        self.t3.setTime(now)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

