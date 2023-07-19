# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor, QFont
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

def draw(self):
    qpainter = QPainter()
    qpainter.begin(MainWindow)

    font = QFont()            # 建立文字樣式物件
    font.setFamily('Times')   # 設定字型
    font.setPointSize(50)     # 設定文字大小
    font.setWeight(87)        # 設定文字粗細
    font.setStyle(QFont.Style.StyleItalic)  # 設定文字樣式
    # font.setStyle(QFont.StyleItalic)  # PyQt5 寫法

    qpainter.setPen(QColor('#ff0000'))
    qpainter.setFont(font)    # 根據文字樣式物件設定文字樣式
    qpainter.drawText(50,50,'hello')  # 放入文字

    qpainter.setPen(QColor('#0000ff'))
    qpainter.setFont(QFont('Arial',30)) # 直接使用 QFont 設定文字樣式
    qpainter.drawText(50,100,'hello')   # 放入文字

    qpainter.end()

MainWindow.paintEvent = draw
MainWindow.show()
sys.exit(app.exec())


