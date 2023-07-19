# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
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
        self.box.setItemIcon(0, QtGui.QIcon('icon.png'))   # 第一個選項
        self.box.setItemIcon(1, QtGui.QIcon('mona.jpg'))   # 第二個選項
        self.box.setItemIcon(2, QtGui.QIcon('orange.jpg')) # 第三個選項
        self.box.setItemIcon(3, QtGui.QIcon('ok.png'))     # 第四個選項

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

