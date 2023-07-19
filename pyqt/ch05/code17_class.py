# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.box = QtWidgets.QComboBox(self)
        self.box.addItems(['A','B','C','D'])
        self.box.setGeometry(10,10,200,30)
        self.box.setCurrentIndex(1)     # 預先顯示第二個選項 ( 第一個為 0 )
        self.box.setCurrentText('D')    # 如果選項文字為 D，則顯示 D

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

