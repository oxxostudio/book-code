# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.ui()

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(10,10,100,30)
        self.btn1.setText('最大化')
        self.btn1.clicked.connect(lambda: self.showMaximized())  # 最大化

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(110,10,100,30)
        self.btn2.setText('恢復大小')
        self.btn2.clicked.connect(lambda: self.showNormal())     # 恢復原本大小

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(10,50,100,30)
        self.btn3.setText('移動視窗')
        self.btn3.clicked.connect(lambda: self.move(100, 100))   # 移動到 (100, 100)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

