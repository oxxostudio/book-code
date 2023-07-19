# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets           # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import pyqtSignal   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class mainWindow(QtWidgets.QWidget):

    signal = pyqtSignal()    # 建立信號物件

    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()
        self.signal.connect(self.signalListener)            # 監聽信號

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('發送信號')
        self.btn.setGeometry(50,60,100,30)
        self.btn.clicked.connect(lambda:self.signal.emit())  # 發送信號

    def signalListener(self):
        print('收到信號')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
sys.exit(app.exec())

