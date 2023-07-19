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
        self.label.setGeometry(20,20,100,30)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setGeometry(20,40,100,30)
        self.slider.setRange(0, 100)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        # self.slider.setOrientation(1)   # PyQt5 寫法
        self.slider.valueChanged.connect(self.showNum)    # 數值改變時連動對應函式

    def showNum(self):
        self.label.setText(str(self.slider.value()))  # 顯示滑桿數值

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

