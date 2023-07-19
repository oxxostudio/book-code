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

            qpen = QPen()                     # 建立 QPen 物件
            qpen.setColor(QColor('#000000'))  # 設定顏色
            qpen.setWidth(5)                  # 設定寬度
            qpen.setStyle(Qt.PenStyle.DotLine)         # 設定樣式
            qpen.setCapStyle(Qt.PenCapStyle.FlatCap)      # 設定線段開頭與結尾樣式
            qpen.setJoinStyle(Qt.PenJoinStyle.MiterJoin)   # 設定線段連接處樣式

            self.qpainter.setPen(qpen)   # 效果等同下方
            # self.qpainter.setPen(QPen(QColor('#000000'), 5, Qt.PenStyle.DotLine, Qt.PenCapStyle.FlatCap, Qt.PenJoinStyle.MiterJoin))
            self.qpainter.drawRect(30,50,100,100)

            self.qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.PenStyle.DashDotDotLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            # self.qpainter.setPen(QPen(QColor('#ff0000'), 10, Qt.DashDotDotLine, Qt.RoundCap, Qt.RoundJoin))    # PyQt5 寫法
            self.qpainter.drawRect(160,50,100,100)

            self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

