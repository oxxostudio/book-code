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

        self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.PenStyle.SolidLine))      # 實線
        # self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.SolidLine))             # PyQt5 寫法
        self.qpainter.drawLine(50, 40, 250, 40)

        self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.PenStyle.DashLine))       # 虛線
        # self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.DashLine))             # PyQt5 寫法
        self.qpainter.drawLine(50, 60, 250, 60)

        self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.PenStyle.DotLine))        # 點狀線
        # self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.DotLine))             # PyQt5 寫法
        self.qpainter.drawLine(50, 80, 250, 80)

        self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.PenStyle.DashDotLine))    # 一點狀線混合虛線
        # self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.DashDotLine))             # PyQt5 寫法
        self.qpainter.drawLine(50, 100, 250, 100)

        self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.PenStyle.DashDotDotLine)) # 兩點狀線混合虛線
        # self.qpainter.setPen(QPen(QColor(0,0,0), 6, Qt.DashDotDotLine))             # PyQt5 寫法
        self.qpainter.drawLine(50, 120, 250, 120)

        qpen = QPen()
        qpen.setColor(QColor(0,0,0))
        qpen.setWidth(6)
        space = 4          # 空白長度
        dashes = [1, space, 3, space, 9, space, 5, space, 1, space] # 自訂虛線樣式，偶數為空白
        qpen.setDashPattern(dashes)        # 設定虛線樣式
        qpen.setStyle(Qt.PenStyle.CustomDashLine)   # 自訂虛線
        # qpen.setStyle(Qt.CustomDashLine)  # PyQt5 寫法
        self.qpainter.setPen(qpen)
        self.qpainter.drawLine(50, 140, 250, 140)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

