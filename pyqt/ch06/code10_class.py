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
        self.d1 = QtWidgets.QDateEdit(self)
        self.d1.setGeometry(20,20,100,30)
        self.d1.setDisplayFormat('dd/MM/yyyy')
        self.d1.setDateRange(QtCore.QDate(2000, 1, 1), QtCore.QDate(2000, 2, 1))  # 設定日期範圍

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

