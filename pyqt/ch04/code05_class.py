# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('hello world, how are you?')
        self.label.setGeometry(20, 20, 200, 150)
        self.label.setWordWrap(True)    # 設定可以換行

        self.label.setStyleSheet('''
            background:#fff;
            color:#f00;
            font-size:20px;
            font-weight:bold;
            border:2px dashed #000;
            padding:20px;
            text-align:center;
        ''')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
