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

    # 左邊的正方形
    qpainter.setPen(QPen(QColor('#000000'), 5, Qt.PenStyle.DotLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.MiterJoin))
    # qpainter.setPen(QPen(QColor('#000000'), 5, Qt.DotLine, Qt.FlatCap, Qt.MiterJoin))  # PyQt5 寫法
    qpainter.drawRect(30,50,100,100)

    # 右邊的正方形
    qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.PenStyle.DashDotDotLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    # qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.DashDotDotLine, Qt.RoundCap, Qt.RoundJoin))  # PyQt5 寫法
    qpainter.drawRect(160,50,100,100)

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

