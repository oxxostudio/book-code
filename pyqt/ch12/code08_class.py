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

        # 左邊的正方形
        self.qpainter.setPen(QPen(QColor('#000000'), 5, Qt.PenStyle.DotLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.MiterJoin))
        # self.qpainter.setPen(QPen(QColor('#000000'), 5, Qt.DotLine, Qt.FlatCap, Qt.MiterJoin))  # PyQt5 寫法
        self.qpainter.drawRect(30,50,100,100)

        # 右邊的正方形
        self.qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.PenStyle.DashDotDotLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
        # self.qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.DashDotDotLine, Qt.RoundCap, Qt.RoundJoin))  # PyQt5 寫法
        self.qpainter.drawRect(160,50,100,100)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

