# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.box1 = QtWidgets.QSpinBox(self)        # 加入整數調整元件
        self.box1.move(30,10)
        self.box1.setRange(0,100)                   # 設定數值調整區間

        self.box2 = QtWidgets.QDoubleSpinBox(self)  # 加入浮點數調整元件
        self.box2.move(100,10)
        self.box2.setRange(0,100)                   # 設定數值調整區間

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())


