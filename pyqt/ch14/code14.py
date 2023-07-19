# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(400, 300)                # 主視窗大小

canvas = QPixmap(400,240)                  # 建立 QPixmap 元件作為畫布，並設定畫布大小
canvas.fill(QColor('#ffffff'))             # 畫布填滿白色

label = QtWidgets.QLabel(MainWindow)       # 建立 QLabel
label.setGeometry(0, 0, 400, 240)          # 設定大小位置，下方留下一些空白
label.setPixmap(canvas)                    # 放入畫布

last_x, last_y = None, None                # 設定兩個變數紀錄滑鼠座標
penSize = 10                               # 畫筆預設粗細
penColor = QColor('#000000')               # 畫筆預設顏色

# 放開滑鼠的函式
def release(self):
    global last_x, last_y
    last_x, last_y = None, None            # 清空座標內容

# 按下滑鼠的函式
def mousePress(self):
    global penColor, penSize, canvas
    mx = int(QEnterEvent.position(self).x())
    my = int(QEnterEvent.position(self).y())
    # mx = int(self.x())  # PyQt5 寫法
    # my = int(self.y())  # PyQt5 寫法
    qpainter = QPainter()                  # 建立 QPainter 元件
    qpainter.begin(canvas)                 # 在畫布中開始繪圖
    qpainter.setPen(QPen(QColor(penColor), penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
    # qpainter.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine, Qt.RoundCap))  # PyQt5 寫法
    qpainter.drawPoint(mx, my)             # 下筆畫出一個點
    qpainter.end()                         # 結束繪圖
    label.setPixmap(canvas)
    MainWindow.update()                    # 更新主視窗內容

# 按下滑鼠並移動滑鼠的函式
def draw(self):
    global last_x, last_y, penColor, penSize, canvas
    mx = int(QEnterEvent.position(self).x())
    my = int(QEnterEvent.position(self).y())
    # mx = int(self.x())  # PyQt5 寫法
    # my = int(self.y())  # PyQt5 寫法
    if last_x is None:
        last_x = mx                 # 紀錄滑鼠當下的座標
        last_y = my
        return
    qpainter = QPainter()          # 建立 QPainter 元件
    qpainter.begin(canvas)         # 在畫布中開始繪圖
    qpainter.setPen(QPen(penColor, penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
    # qpainter.setPen(QPen(penColor, penSize, Qt.SolidLine, Qt.RoundCap))  # PYQt5 寫法
    qpainter.drawLine(last_x, last_y, mx, my) # 下筆畫出一條線
    qpainter.end()                 # 結束繪圖
    label.setPixmap(canvas)
    MainWindow.update()            # 更新主視窗內容
    last_x = mx                    # 紀錄結束座標
    last_y = my

label.mousePressEvent  = mousePress        # 設定按下滑鼠並移動的事件
label.mouseMoveEvent = draw                # 設定按下滑鼠的事件
label.mouseReleaseEvent = release          # 設定放開滑鼠的事件

MainWindow.show()
sys.exit(app.exec())

