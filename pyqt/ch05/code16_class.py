# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.box = QtWidgets.QComboBox(self)   # 加入下拉選單
        self.box.addItems(['A','B','C','D'])   # 加入四個選項
        self.box.setGeometry(10,10,200,30)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

