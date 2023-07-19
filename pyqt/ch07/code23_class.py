# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10,50,200,50)
        self.label.setStyleSheet('font-size:30px;')

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(10,10,100,30)
        self.btn1.setText('整數')
        self.btn1.clicked.connect(self.showInt)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(110,10,100,30)
        self.btn2.setText('浮點數')
        self.btn2.clicked.connect(self.showDouble)

    def showInt(self):
        num, ok = QtWidgets.QInputDialog().getInt(self, '', '請輸入一個整數')
        self.label.setText(str(num))

    def showDouble(self):
        num, ok = QtWidgets.QInputDialog().getDouble(self, '', '請輸入一個浮點數')
        self.label.setText(str(num))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

