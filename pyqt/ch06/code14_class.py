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
        self.slider_1 = QtWidgets.QSlider(self)
        self.slider_1.move(20,20)
        self.slider_1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_1.setTickPosition(self.slider_1.TickPosition.TicksAbove) # 下方加入刻度線
        # self.slider_1.setOrientation(1)   # PyQt5 寫法
        # self.slider_1.setTickPosition(2)  # PyQt5 寫法
        self.slider_1.setTickInterval(10)         # 刻度線間距 ( 會有十條刻度線 )

        self.slider_2 = QtWidgets.QSlider(self)
        self.slider_2.move(20,60)
        self.slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_2.setTickPosition(self.slider_1.TickPosition.TicksBothSides) # 上下都加入刻度線
        # self.slider_2.setOrientation(1)   # PyQt5 寫法
        # self.slider_2.setTickPosition(3)  # PyQt5 寫法
        self.slider_2.setTickInterval(20)   # 刻度線間距 ( 會有五條刻度線 )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

