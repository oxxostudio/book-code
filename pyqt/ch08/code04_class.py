# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        box = QtWidgets.QWidget(self)        # 建立放 QGridLayout 的元件
        box.setGeometry(10,10,150,150)       # 指定大小位置

        grid = QtWidgets.QGridLayout(box)    # 建立 QGridLayout

        btn1 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn1.setText('1')
        grid.addWidget(btn1, 0, 0)           # 按鈕放在 (0, 0) 位置

        btn2 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn2.setText('2')
        grid.addWidget(btn2, 0, 1)           # 按鈕放在 (0, 1) 位置

        btn3 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn3.setText('3')
        grid.addWidget(btn3, 0, 2)           # 按鈕放在 (0, 2) 位置

        btn4 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn4.setText('4')
        grid.addWidget(btn4, 1, 0)           # 按鈕放在 (1, 0) 位置

        btn5 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn5.setText('5')
        grid.addWidget(btn5, 1, 1)           # 按鈕放在 (1, 1) 位置

        btn6 = QtWidgets.QPushButton(self)   # 建立按鈕
        btn6.setText('6')
        grid.addWidget(btn6, 1, 2)           # 按鈕放在 (1, 2) 位置

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

