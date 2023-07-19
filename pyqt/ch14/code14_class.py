# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.last_x, self.last_y = None, None   # 設定兩個變數紀錄滑鼠座標
        self.penSize = 10                       # 畫筆預設粗細
        self.penColor = QColor('#000000')       # 畫筆預設顏色
        self.ui()

    def ui(self):
        self.canvas = QPixmap(400,240)          # 建立 QPixmap 元件作為畫布，並設定畫布大小
        self.canvas.fill(QColor('#ffffff'))     # 畫布填滿白色

        self.label = QtWidgets.QLabel(self)     # 建立 QLabel
        self.label.setGeometry(0, 0, 400, 240)  # 設定大小位置，下方留下一些空白
        self.label.setPixmap(self.canvas)       # 放入畫布

    def mousePressEvent(self, event):
        mx = int(QEnterEvent.position(event).x())
        my = int(QEnterEvent.position(event).y())
        # mx = int(self.x())  # PyQt5 寫法
        # my = int(self.y())  # PyQt5 寫法
        qpainter = QPainter()                  # 建立 QPainter 元件
        qpainter.begin(self.canvas)            # 在畫布中開始繪圖
        qpainter.setPen(QPen(QColor(self.penColor), self.penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
        # qpainter.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine, Qt.RoundCap))  # PyQt5 寫法
        qpainter.drawPoint(mx, my)             # 下筆畫出一個點
        qpainter.end()                         # 結束繪圖
        self.label.setPixmap(self.canvas)
        self.update()                          # 更新主視窗內容

    def mouseMoveEvent(self, event):
        mx = int(QEnterEvent.position(event).x())
        my = int(QEnterEvent.position(event).y())
        # mx = int(self.x())  # PyQt5 寫法
        # my = int(self.y())  # PyQt5 寫法
        if self.last_x is None:
            self.last_x = mx                 # 紀錄滑鼠當下的座標
            self.last_y = my
            return
        qpainter = QPainter()                # 建立 QPainter 元件
        qpainter.begin(self.canvas)          # 在畫布中開始繪圖
        qpainter.setPen(QPen(self.penColor, self.penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
        # qpainter.setPen(QPen(penColor, penSize, Qt.SolidLine, Qt.RoundCap))  # PYQt5 寫法
        qpainter.drawLine(self.last_x, self.last_y, mx, my) # 下筆畫出一條線
        qpainter.end()                      # 結束繪圖
        self.label.setPixmap(self.canvas)
        self.update()                       # 更新主視窗內容
        self.last_x = mx                    # 紀錄結束座標
        self.last_y = my

    def mouseReleaseEvent(self, event):
        self.last_x, self.last_y = None, None   # 清空座標內容

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

