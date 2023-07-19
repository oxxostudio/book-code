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

    qpainter.setPen(QPen(QColor('#000000'), 10))
    qpainter.drawLine(50,25,250,25)

    pen = QPen()                       # 建立畫筆樣式物件
    pen.setStyle(Qt.PenStyle.DashDotLine)  # 設定樣式為 Qt.DashDotLine ( Qt 在 PyQt6.QtCore 裡 )
    # pen.setStyle(Qt.DashDotLine)     # PyQt5 寫法
    pen.setColor(QColor('#000000'))    # 設定顏色
    pen.setWidth(5)                    # 設定粗細
    qpainter.setPen(pen)
    qpainter.drawLine(50,50,250,50)

    pen = QPen()                       # 建立畫筆樣式物件
    pen.setStyle(Qt.PenStyle.DotLine)  # 設定樣式為 Qt.DotLine ( Qt 在 PyQt6.QtCore 裡 )
    # pen.setStyle(Qt.DotLine)     # PyQt5 寫法
    pen.setColor(QColor('#000000'))    # 設定顏色
    pen.setWidth(2)                    # 設定粗細
    qpainter.setPen(pen)
    qpainter.drawLine(50,75,250,75)

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

