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
        self.label.setGeometry(10,10,50,30)
        self.box1 = QtWidgets.QSpinBox(self)
        self.box1.move(80,10)
        self.box1.setRange(0,100)
        self.box1.setSingleStep(1)
        self.box1.setValue(50)
        self.box1.valueChanged.connect(self.showText)   # 調整時執行函式

    def showText(self):
        self.label.setText(str(self.box1.value()))  # 顯示調整數值

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

