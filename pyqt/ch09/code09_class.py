# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets           # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import pyqtSignal   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):

    signal = pyqtSignal(str)      # 建立 pyqtSignal 物件，傳遞字串格式內容

    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()
        self.signal.connect(self.showMsg)    # 建立插槽監聽信號

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('A')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('B')
        self.btn2.setGeometry(110,60,50,30)
        self.btn2.clicked.connect(lambda:self.signal.emit('B'))  # 發送字串信號 B

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('A')
        self.btn1.setGeometry(50,60,50,30)
        self.btn1.clicked.connect(lambda:self.signal.emit('A'))  # 發送字串信號 A

    def showMsg(self, val):
        self.label.setText(val)   # 顯示內容

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

