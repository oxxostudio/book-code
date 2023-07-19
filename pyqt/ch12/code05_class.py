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

        self.qpainter.setPen(QPen(QColor('#000000'), 10))
        self.qpainter.drawLine(50,25,250,25)

        self.pen = QPen()                       # 建立畫筆樣式物件
        self.pen.setStyle(Qt.PenStyle.DashDotLine)  # 設定樣式為 Qt.DashDotLine ( Qt 在 PyQt6.QtCore 裡 )
        # self.pen.setStyle(Qt.DashDotLine)     # PyQt5 寫法
        self.pen.setColor(QColor('#000000'))    # 設定顏色
        self.pen.setWidth(5)                    # 設定粗細
        self.qpainter.setPen(self.pen)
        self.qpainter.drawLine(50,50,250,50)

        self.pen = QPen()                       # 建立畫筆樣式物件
        self.pen.setStyle(Qt.PenStyle.DotLine)  # 設定樣式為 Qt.DotLine ( Qt 在 PyQt6.QtCore 裡 )
        # self.pen.setStyle(Qt.DotLine)         # PyQt5 寫法
        self.pen.setColor(QColor('#000000'))    # 設定顏色
        self.pen.setWidth(2)                    # 設定粗細
        self.qpainter.setPen(self.pen)
        self.qpainter.drawLine(50,75,250,75)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

