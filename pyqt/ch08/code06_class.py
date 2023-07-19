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
        style_box = '''
            background:#fff;
            border:1px solid #000;
        '''

        style_btn = '''
            background:#ff0;
            padding:5px;
            border-radius:4px;
        '''

        box = QtWidgets.QWidget(self)
        box.setGeometry(10,10,150,150)
        box.setStyleSheet(style_box)

        grid = QtWidgets.QGridLayout(box)

        btn1 = QtWidgets.QPushButton(self)
        btn1.setText('1')
        btn1.setStyleSheet(style_btn)
        grid.addWidget(btn1, 0, 0)

        btn2 = QtWidgets.QPushButton(self)
        btn2.setText('2')
        grid.addWidget(btn2, 0, 1)

        btn3 = QtWidgets.QPushButton(self)
        btn3.setText('3')
        grid.addWidget(btn3, 0, 2)

        btn4 = QtWidgets.QPushButton(self)
        btn4.setText('4')
        grid.addWidget(btn4, 1, 0, 1, 3)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

