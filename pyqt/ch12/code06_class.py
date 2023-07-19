# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)

    def paintEvent(self, event):
        self.qpainter = QPainter()
        self.qpainter.begin(self)

        qimage = QImage('mona.jpg')
        w = qimage.size().width()
        h = qimage.size().height()
        self.qpainter.drawImage(QRect(20, 20, w, h), qimage)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

