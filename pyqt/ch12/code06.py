# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

def draw(self):
    qpainter = QPainter()
    qpainter.begin(MainWindow)

    qimage = QImage('mona.jpg')
    w = qimage.size().width()
    h = qimage.size().height()
    qpainter.drawImage(QRect(20, 20, w, h), qimage)

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

