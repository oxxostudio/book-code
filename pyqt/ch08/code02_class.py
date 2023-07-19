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
        self.vbox = QtWidgets.QWidget(self)
        self.vbox.setGeometry(0,0,150,150)

        self.v_layout = QtWidgets.QVBoxLayout(self.vbox)
        self.v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # 靠左對齊
        # self.v_layout.setAlignment(QtCore.Qt.AlignLeft)              # PyQt5 寫法

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('1')
        self.v_layout.addWidget(self.btn1)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('2')
        self.v_layout.addWidget(self.btn2)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText('3')
        self.v_layout.addWidget(self.btn3)

        self.hbox = QtWidgets.QWidget(self)
        self.hbox.setGeometry(150,0,150,150)

        self.h_layout = QtWidgets.QHBoxLayout(self.hbox)
        self.h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop) # 靠上對齊
        # self.h_layout.setAlignment(QtCore.Qt.AlignTop)             # PyQt5 寫法

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText('4')
        self.h_layout.addWidget(self.btn4)

        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setText('5')
        self.h_layout.addWidget(self.btn5)

        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.setText('6')
        self.h_layout.addWidget(self.btn6)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

