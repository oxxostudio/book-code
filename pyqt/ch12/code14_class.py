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
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)     # 建立 QLabel
        self.label.setGeometry(0, 20, 300, 180) # 設定位置 ( 最上方留下 20px 空間 )
        self.canvas = QPixmap(300,180)          # 新增 QPixmap 物件為畫布
        self.canvas.fill(QColor('#ffdddd'))     # 設定畫布背景

    def paintEvent(self, event):
        self.qpainter = QPainter()              # 建立 QPainter() 物件
        self.qpainter.begin(self.canvas)        # 綁定 canvas 進行繪畫

        self.qpainter.setPen(QPen(QColor('#ff0000'), 5))  # 繪製紅色矩形
        self.qpainter.drawRect(10,10,100,100)

        self.qpainter.setPen(QPen(QColor('#00aa00'), 5))  # 繪製綠色橢圓
        self.qpainter.drawEllipse(50, 50, 100, 100)

        self.qpainter.setPen(QPen(QColor('#000000'), 5))  # 繪製黑色直線
        self.qpainter.drawLine(100,100,300,200)

        self.qpainter.end()                      # 繪圖結束
        self.label.setPixmap(self.canvas)        # 將 canvas 放入 QLabel 中

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

