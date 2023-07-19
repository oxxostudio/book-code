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
        self.label.setGeometry(20,20,120,30)

        self.d1 = QtWidgets.QDateEdit(self)
        self.d1.setGeometry(150,20,100,30)
        self.d1.setDisplayFormat('dd/MM/yyyy')
        self.d1.setDate(QtCore.QDate().currentDate())  # 設定日期為目前日期
        self.d1.dateChanged.connect(self.showDate)     # 執行函式

    def showDate(self):
        self.label.setText(self.d1.date().toString())   # 顯示目前日期

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

