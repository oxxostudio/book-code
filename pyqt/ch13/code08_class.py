# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)

    def paintEvent(self, event):
        qpainter = QPainter()
        qpainter.begin(self)

        qimage = QImage('mona.jpg')
        qpainter.drawImage(QRect(0, 0, 100, 150), qimage)      # 修改位置和尺寸
        qpainter.drawImage(QRect(150, 30, 150, 150), qimage)   # 修改位置和尺寸

        qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

