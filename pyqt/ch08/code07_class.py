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
        box = QtWidgets.QWidget(self)
        box.setGeometry(10,10,150,150)

        grid = QtWidgets.QGridLayout(box)

        btn1 = QtWidgets.QPushButton(self)
        btn1.setText('1')
        grid.addWidget(btn1, 0, 0)

        btn2 = QtWidgets.QPushButton(self)
        btn2.setText('2')
        grid.addWidget(btn2, 0, 1)

        btn3 = QtWidgets.QPushButton(self)
        btn3.setText('3')
        grid.addWidget(btn3, 0, 2)

        grid2 = QtWidgets.QGridLayout(box)    # 新建一個 QGridLayout
        grid.addItem(grid2, 1, 0, 1, 3)       # 使用 addItem 方法

        btn4 = QtWidgets.QPushButton(self)
        btn4.setText('4')
        grid2.addWidget(btn4, 0, 0)           # 新的 QGridLayout 加入按鈕

        btn5 = QtWidgets.QPushButton(self)
        btn5.setText('5')
        grid2.addWidget(btn5, 0, 1)           # 新的 QGridLayout 加入按鈕

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

