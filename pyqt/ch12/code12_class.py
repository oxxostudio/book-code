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

        self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap))
        # self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.SolidLine, Qt.FlatCap))  # PyQt5
        self.qpainter.drawLine(50, 40, 250, 40)

        self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap))
        # self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.SolidLine, Qt.FlatCap))  # PyQt5
        self.qpainter.drawLine(50, 80, 250, 80)

        self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap))
        # self.qpainter.setPen(QPen(QColor(0,0,0), 2, Qt.SolidLine, Qt.FlatCap))  # PyQt5
        self.qpainter.drawLine(50, 120, 250, 120)

        self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.PenStyle.SolidLine, Qt.PenCapStyle.SquareCap))
        # self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.SolidLine, Qt.SquareCap))  # PyQt5
        self.qpainter.drawLine(50, 40, 250, 40)

        self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap))
        # self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.SolidLine, Qt.FlatCap))  # PyQt5
        self.qpainter.drawLine(50, 80, 250, 80)

        self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        # self.qpainter.setPen(QPen(QColor(255,0,0,50), 20, Qt.SolidLine, Qt.RoundCap))  # PyQt5
        self.qpainter.drawLine(50, 120, 250, 120)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

