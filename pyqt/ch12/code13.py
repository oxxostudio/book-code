# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

def draw(self):
    qpainter = QPainter()
    qpainter.begin(MainWindow)

    qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.BevelJoin))
    # qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.BevelJoin))   # PyQt5
    points = [QPoint(30,160),QPoint(60,50),QPoint(90,160)]
    qpainter.drawPolyline(points)

    qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.MiterJoin))
    # qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.MiterJoin))   # PyQt5
    points = [QPoint(120,160),QPoint(150,50),QPoint(180,160)]
    qpainter.drawPolyline(points)

    qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.RoundJoin))
    # qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.RoundJoin))   # PyQt5
    points = [QPoint(210,160),QPoint(240,50),QPoint(270,160)]
    qpainter.drawPolyline(points)

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

