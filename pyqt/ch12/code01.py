# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QPainter, QColor, QPen   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

# 定義繪圖的函式，注意需要包含 self 參數
def draw(self):
    qpainter = QPainter()                # 建立繪圖器
    qpainter.begin(MainWindow)           # 在 MainWindow 開始繪圖

    qpainter.setPen(QPen(QColor('#ff0000'),5))  # 設定畫筆顏色和寬度
    qpainter.drawRect(50, 50, 100, 100)  # 繪製正方形

    qpainter.end()                       # 結束繪圖

MainWindow.paintEvent = draw             # 設定 paintEvent 屬性
MainWindow.show()
sys.exit(app.exec())

