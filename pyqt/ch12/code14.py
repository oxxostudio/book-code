# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)   # 建立 QLabel
label.setGeometry(0, 20, 300, 180)     # 設定位置 ( 最上方留下 20px 空間 )

def draw(self):
    canvas = QPixmap(300,180)          # 新增 QPixmap 物件為畫布
    canvas.fill(QColor('#ffdddd'))     # 設定畫布背景
    qpainter = QPainter()              # 建立 QPainter() 物件
    qpainter.begin(canvas)             # 綁定 canvas 進行繪畫

    qpainter.setPen(QPen(QColor('#ff0000'), 5))  # 繪製紅色矩形
    qpainter.drawRect(10,10,100,100)

    qpainter.setPen(QPen(QColor('#00aa00'), 5))  # 繪製綠色橢圓
    qpainter.drawEllipse(50, 50, 100, 100)

    qpainter.setPen(QPen(QColor('#000000'), 5))  # 繪製黑色直線
    qpainter.drawLine(100,100,300,200)

    qpainter.end()                      # 繪圖結束
    label.setPixmap(canvas)             # 將 canvas 放入 QLabel 中

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

