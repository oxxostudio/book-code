# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

def draw(self):
    qpainter = QPainter()
    qpainter.begin(MainWindow)

    qpainter.setPen(QPen(QColor('#ff0000'), 5))
    qpainter.drawRect(10,10,100,100)

    qpainter.setPen(QPen(QColor('#00aa00'), 5))
    qpainter.drawEllipse(50, 50, 100, 100)

    qpainter.setPen(QPen(QColor('#000000'), 5))
    qpainter.drawLine(100,100,300,200)

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

