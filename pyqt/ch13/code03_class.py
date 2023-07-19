# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)    #  建立 QLabel
        self.label.setGeometry(0, 0, 300, 200)
        self.label2 = QtWidgets.QLabel(self)   #  建立 QLabel
        self.label2.setGeometry(0, 0, 300, 200)
        self.label2.move(0, -50)               # 調整位置

        qpixmap = QPixmap()
        qpixmap.load('mona.jpg')
        img1 = qpixmap.scaled(300,50)          # 建立圖片 1
        self.label.setPixmap(img1)             # 加入圖片 1
        img2 = qpixmap.scaled(150,200)         # 建立圖片 2
        self.label2.setPixmap(img2)            # 加入圖片 2

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

