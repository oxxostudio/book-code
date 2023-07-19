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
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 300, 200)

        qpixmap = QPixmap()
        qimg = QImage('mona.jpg')            # 讀取圖片
        qpixmap = qpixmap.fromImage(qimg)    # 將圖片加入 QPixmap 物件中
        self.label.setPixmap(qpixmap)        # 將 QPixmap 物件加入到 label 裡

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

