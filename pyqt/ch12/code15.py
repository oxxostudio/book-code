# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 30, 300, 170)

def save(format):
    if format == 'jpg':
        label.pixmap().save('demo.jpg','JPG',90)   # 儲存為 jpg
    else:
        label.pixmap().save('demo.png','PNG')      # 儲存為 png

btn1 = QtWidgets.QPushButton(MainWindow)
btn1.setText('儲存為 jpg')
btn1.setGeometry(20,0,100,30)
btn1.clicked.connect(lambda: save('jpg'))   # 綁定儲存的函式

btn2 = QtWidgets.QPushButton(MainWindow)
btn2.setText('儲存為 png')
btn2.setGeometry(120,0,100,30)
btn2.clicked.connect(lambda: save('png'))   # 綁定儲存的函式

def draw(self):
    canvas = QPixmap(300,170)
    canvas.fill(QColor('#ffdddd'))
    qpainter = QPainter()
    qpainter.begin(canvas)

    qpainter.setPen(QPen(QColor('#ff0000'), 5))
    qpainter.drawRect(10,10,100,100)

    qpainter.setPen(QPen(QColor('#00aa00'), 5))
    qpainter.drawEllipse(50, 50, 100, 100)

    qpainter.setPen(QPen(QColor('#000000'), 5))
    qpainter.drawLine(100,100,300,200)

    qpainter.end()
    label.setPixmap(canvas)

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())

