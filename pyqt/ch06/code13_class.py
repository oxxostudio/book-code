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
        self.slider_1 = QtWidgets.QSlider(self)   # 預設垂直
        self.slider_1.move(20,20)

        self.slider_2 = QtWidgets.QSlider(self)
        self.slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)  # 設定為水平
        # self.slider_2.setOrientation(1)    # 這行是 PyQt5 寫法：設定為水平
        self.slider_2.move(50,20)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

