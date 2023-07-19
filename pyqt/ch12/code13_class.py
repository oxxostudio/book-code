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
        self.resize(300, 200)

    def paintEvent(self, event):
        self.qpainter = QPainter()
        self.qpainter.begin(self)

        self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.BevelJoin))
        # self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.BevelJoin))   # PyQt5
        points = [QPoint(30,160),QPoint(60,50),QPoint(90,160)]
        self.qpainter.drawPolyline(points)

        self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.MiterJoin))
        # self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.MiterJoin))   # PyQt5
        points = [QPoint(120,160),QPoint(150,50),QPoint(180,160)]
        self.qpainter.drawPolyline(points)

        self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.RoundJoin))
        # self.qpainter.setPen(QPen(QColor(255,0,0), 25, Qt.SolidLine, Qt.FlatCap, Qt.RoundJoin))   # PyQt5
        points = [QPoint(210,160),QPoint(240,50),QPoint(270,160)]
        self.qpainter.drawPolyline(points)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

